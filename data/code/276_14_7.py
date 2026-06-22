def read_tasks(file_path):
    tasks = []
    with open(file_path, 'r') as file:
        for line in file:
            task, priority = line.strip().split(',')
            tasks.append((task, int(priority)))
    return tasks

def execute_tasks(tasks):
    tasks.sort(key=lambda x: x[1], reverse=True)
    while tasks:
        highest_priority_task = tasks.pop(0)
        print(f"Executing {highest_priority_task[0]} with priority {highest_priority_task[1]}")

if __name__ == '__main__':
    sample_tasks = read_tasks('tasks.txt')
    execute_tasks(sample_tasks)