class TaskScheduler:
    def __init__(self, tasks_file):
        self.tasks = []
        with open(tasks_file, 'r') as file:
            for line in file:
                task, priority = line.strip().split(',')
                self.tasks.append((task, int(priority)))

    def execute_tasks(self):
        while self.tasks:
            highest_priority = max(task[1] for task in self.tasks)
            tasks_to_execute = [task for task in self.tasks if task[1] == highest_priority]
            for task in tasks_to_execute:
                print(f"Executing: {task[0]}")
                self.tasks.remove(task)

if __name__ == '__main__':
    scheduler = TaskScheduler('tasks.txt')
    scheduler.execute_tasks()