import heapq

def read_tasks(filename):
    tasks = []
    with open(filename, 'r') as file:
        for line in file:
            priority, task = line.strip().split(' ', 1)
            tasks.append((int(priority), task))
    return tasks

def execute_tasks(tasks):
    heap = []
    for priority, task in tasks:
        heapq.heappush(heap, (priority, task))
    
    while heap:
        _, task = heapq.heappop(heap)
        print(f"Executing: {task}")

if __name__ == '__main__':
    tasks = read_tasks('tasks.txt')
    execute_tasks(tasks)