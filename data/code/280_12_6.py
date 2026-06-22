def repeat_task(times):
    for _ in range(times):
        yield "Task executed"

if __name__ == '__main__':
    task_repeater = repeat_task(10)
    repeated_tasks = list(task_repeater)
    print(repeated_tasks)