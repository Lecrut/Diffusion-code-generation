class TaskScheduler:
    def __init__(self):
        self.tasks = []

    @staticmethod
    def parse_task(task_str):
        priority, description = task_str.split(maxsplit=1)
        return int(priority), description

    def add_task(self, task_str):
        priority, description = self.parse_task(task_str)
        self.tasks.append((priority, description))

    def execute_tasks(self):
        while self.tasks:
            highest_priority = max(self.tasks)[0]
            tasks_to_execute = [task for task in self.tasks if task[0] == highest_priority]
            for _, task_desc in sorted(tasks_to_execute, key=lambda x: x[1]):
                print(f"Executing: {task_desc}")
            self.tasks = [task for task in self.tasks if task[0] != highest_priority]

if __name__ == '__main__':
    scheduler = TaskScheduler()
    scheduler.add_task("2 Move the robot")
    scheduler.add_task("1 Pick up object")
    scheduler.add_task("2 Place object")
    scheduler.add_task("1 Check sensors")
    scheduler.execute_tasks()