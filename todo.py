
import json

tasks = []
def get_next_task_id(tasks):
    task_id = 1

    existing_ids = {task["id"] for task in tasks}

    while task_id in existing_ids:
        task_id += 1

    return task_id
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    task_id = get_next_task_id(tasks)
    tasks.append({"id": task_id, "title": title, "completed": False})
    print(f"Task '{title}' added with ID {task_id}.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- To-Do List ---")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['id']}, Task: {task['title']}, Status: {status}")


def complete_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    try:
        task_id = int(input("Enter task ID to mark as completed: "))
    except ValueError:
        print("Please enter a valid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print(f"Task '{task['title']}' is already completed.")
            else:
                task["completed"] = True
                print(f"Task '{task['title']}' marked as completed.")
            return

    print(f"Task with ID {task_id} not found.")
    
def delete_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task '{task['title']}' deleted successfully.")
            return

    print(f"Task with ID {task_id} not found.")
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved successfully.")
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)

        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()