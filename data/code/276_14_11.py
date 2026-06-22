import re
LOW_PRIORITY = 1
MEDIUM_PRIORITY = 2
HIGH_PRIORITY = 3

class TaskScheduler:

    def __init__(self, tasks_file):
        self.tasks_file = tasks_file
        self.tasks = []

    def read_tasks(self):
        with open(self.tasks_file, 'r') as file:
            for line in file:
                task, priority = re.split('\\s+', line.strip())
                self.tasks.append((task, int(priority)))

    def execute_tasks(self):
        self.read_tasks()
        sorted_tasks = sorted(self.tasks, key=lambda x: (-x[1], x[0]))
        while sorted_tasks:
            highest_priority_tasks = [t for t in sorted_tasks if t[1] == sorted_tasks[0][1]]
            for task, _ in highest_priority_tasks:
                print(f'Executing task: {task}')
            sorted_tasks = [t for t in sorted_tasks if t[1] != sorted_tasks[0][1]]
if __name__ == '__main__':
    scheduler = TaskScheduler('tasks.txt')
    scheduler.execute_tasks()