# To-Do List Application

# Function to display the menu options
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Function to view all tasks
def view_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks in the list.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

# Function to add a new task
def add_task(task_list):
    task = input("Enter a new task: ")  # Prompt the user to enter a task
    task_list.append(task)  # Add the entered task to the task list
    print(f"Task '{task}' added successfully!")

# Function to remove a task by its index
def remove_task(task_list):
    try:
        task_index = int(input("Enter the task number to remove: "))  # Ask the user for the task number
        if task_index < 1 or task_index > len(task_list):  # Check if the task number is valid
            print("Invalid task number.")
        else:
            removed_task = task_list.pop(task_index - 1)  # Remove the task at the specified index
            print(f"Task '{removed_task}' removed successfully!")
    except ValueError:
        print("Invalid input! Please enter a number.")  # Handle invalid input if user enters non-integer

# Main function to run the application
def main():
    task_list = []  # Initialize an empty list to store tasks

    while True:
        show_menu()  # Display the menu options
        choice = input("Choose an option (1-4): ")  # Prompt the user to choose an option

        if choice == '1':
            view_tasks(task_list)  # View all tasks
        elif choice == '2':
            add_task(task_list)  # Add a new task
        elif choice == '3':
            remove_task(task_list)  # Remove a task
        elif choice == '4':
            print("Exiting the application. Goodbye!")  # Exit the application
            break  # End the loop
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")  # Handle invalid menu choice

if __name__ == "__main__":
    main()  # Call the main function to start the program
