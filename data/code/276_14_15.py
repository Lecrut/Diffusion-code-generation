import heapq

def read_tasks(filename):
    tasks = []
    with open(filename, 'r') as file:
        for line in file:
            priority, task = line.strip().split(' ', 1)
            tasks.append((int(priority), task))
    return tasks

def execute_tasks(tasks):
    heapq.heapify(tasks)
    while tasks:
        priority, task = heapq.heappop(tasks)
        print(f"Executing task: {task} with priority: {priority}")

if __name__ == '__main__':
    tasks = read_tasks('tasks.txt')
    execute_tasks(tasks)