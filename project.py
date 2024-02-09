class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if self.tasks:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')
        else:
            print("\nYour To-Do List is empty.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task index.")
todo_list = ToDoList()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        new_task = input("Enter the task: ")
        todo_list.add_task(new_task)
    elif choice == '2':
        todo_list.view_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task index to remove: "))
        todo_list.remove_task(task_index)
    elif choice == '4':
        print("Exiting the To-Do List app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
