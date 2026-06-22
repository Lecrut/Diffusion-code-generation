import heapq

def read_tasks(file_path):
    tasks = []
    with open(file_path, 'r') as file:
        for line in file:
            priority, task = line.strip().split(maxsplit=1)
            tasks.append((int(priority), task))
    return tasks

def execute_tasks(tasks):
    heapq.heapify(tasks)
    while tasks:
        _, task = heapq.heappop(tasks)
        print(f"Executing: {task}")

if __name__ == '__main__':
    sample_file_path = 'tasks.txt'
    tasks = read_tasks(sample_file_path)
    execute_tasks(tasks)