class TaskScheduler:
    def __init__(self, filename):
        self.tasks = []
        with open(filename, 'r') as file:
            for line in file:
                task, priority = line.strip().split(',')
                self.tasks.append((int(priority), task))

    def execute_tasks(self):
        while self.tasks:
            highest_priority = max(task[0] for task in self.tasks)
            tasks_to_execute = [task for task in self.tasks if task[0] == highest_priority]
            for priority, task in sorted(tasks_to_execute, key=lambda x: x[1]):
                print(f"Executing {task}")
                self.tasks.remove((priority, task))

if __name__ == '__main__':
    scheduler = TaskScheduler('tasks.txt')
    scheduler.execute_tasks()