
tasks = []

def show_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- YOUR TO-DO LIST ---")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['name']}")

def add_task():
    name = input("Enter a task: ")
    tasks.append({"name": name, "completed": False})
    print("Task added successfully!")

def complete_task():
    show_tasks()
    try:
        number = int(input("Enter task number to complete: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted task: {removed['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye! Have a productive day.")
        break
    else:
        print("Invalid choice. Please try again.")
