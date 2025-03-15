import streamlit as st
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def main():
    st.set_page_config(page_title="Colorful To-Do List", page_icon="✅", layout="centered")
    
    # Custom CSS for a colorful UI
    st.markdown("""
        <style>
            body {
                background-color: #f0f0f5;
            }
            .stApp {
                background-color: #f5f7fa;
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #ff5733;
                text-align: center;
            }
            .task-card {
                background-color: #fff;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("To-Do List Manager")
    tasks = load_tasks()
    
    # Input section
    new_task = st.text_input("✏️ Enter a new task:")
    if st.button("➕ Add Task", help="Click to add task", key="add_task", use_container_width=True):
        if new_task:
            tasks.append({"task": new_task, "done": False})
            save_tasks(tasks)
            st.experimental_rerun()
    
    # Task List
    st.subheader("📋 Your Tasks")
    if not tasks:
        st.write("🎉 No tasks found! Enjoy your free time!")
    else:
        for index, task in enumerate(tasks):
            col1, col2, col3 = st.columns([6, 1, 1])
            status_icon = "✅" if task["done"] else "❌"
            col1.markdown(f"<div class='task-card'>{index + 1}. {task['task']} {status_icon}</div>", unsafe_allow_html=True)
            if col2.button("✔️ Complete", key=f"complete_{index}"):
                tasks[index]["done"] = True
                save_tasks(tasks)
                st.experimental_rerun()
            if col3.button("🗑️ Remove", key=f"remove_{index}"):
                tasks.pop(index)
                save_tasks(tasks)
                st.experimental_rerun()

if __name__ == "__main__":
    main()
