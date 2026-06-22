def repeat_task(times):
    for _ in range(times):
        yield "Task repeated"

if __name__ == '__main__':
    task_repeater = repeat_task(10)
    repeated_actions = list(task_repeater)
    print(repeated_actions)