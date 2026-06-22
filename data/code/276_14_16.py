import heapq

def read_tasks(filename):
    tasks = []
    with open(filename, 'r') as file:
        for line in file:
            priority, task = line.strip().split(' ', 1)
            heapq.heappush(tasks, (int(priority), task))
    return tasks

def execute_tasks(tasks):
    while tasks:
        _, task = heapq.heappop(tasks)
        print(f"Executing: {task}")

if __name__ == '__main__':
    tasks = read_tasks('tasks.txt')
    execute_tasks(tasks)