#SAMPLE-TASK-LIST
#Develop a Python task management app for adding, removing, listing, prioritizing, and receiving task recommendations based on task descriptions.
import heapq

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 0
        self.priority_queue = []

    def add_task(self, description, priority=0):
        task = {
            'id': self.task_id_counter,
            'description': description,
            'priority': priority
        }
        self.tasks.append(task)
        heapq.heappush(self.priority_queue, (-priority, self.task_id_counter, task))
        self.task_id_counter += 1
        print(f"Added task: {description} with priority {priority}")

    def remove_task(self, task_id):
        task_to_remove = None
        for task in self.tasks:
            if task['id'] == task_id:
                task_to_remove = task
                break
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            self.priority_queue = [t for t in self.priority_queue if t[2]['id'] != task_id]
            heapq.heapify(self.priority_queue)
            print(f"Removed task with ID: {task_id}")
        else:
            print(f"No task found with ID: {task_id}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Task list:")
        for task in self.tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}")

    def prioritize_tasks(self):
        print("Tasks sorted by priority:")
        for _, _, task in sorted(self.priority_queue, reverse=True):
            print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}")

    def recommend_tasks(self, keyword):
        print(f"Tasks related to '{keyword}':")
        related_tasks = [task for task in self.tasks if keyword.lower() in task['description'].lower()]
        if not related_tasks:
            print(f"No tasks found related to '{keyword}'")
        else:
            for task in related_tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}")

if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Tasks")
        print("5. Recommend Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (0 for low, higher for more priority): "))
            manager.add_task(description, priority)
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            manager.remove_task(task_id)
        elif choice == '3':
            manager.list_tasks()
        elif choice == '4':
            manager.prioritize_tasks()
        elif choice == '5':
            keyword = input("Enter keyword to search for related tasks: ")
            manager.recommend_tasks(keyword)
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid option, please try again.")
