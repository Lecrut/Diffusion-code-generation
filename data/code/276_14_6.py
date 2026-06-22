class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority):
        self.tasks.append((task, priority))
        self.tasks.sort(key=lambda x: x[1], reverse=True)

    def execute_tasks(self):
        while self.tasks:
            _, task = self.tasks.pop(0)
            print(f"Executing task: {task}")

if __name__ == '__main__':
    scheduler = TaskScheduler()
    scheduler.add_task("Task 1", 3)
    scheduler.add_task("Task 2", 1)
    scheduler.add_task("Task 3", 2)
    scheduler.execute_tasks()