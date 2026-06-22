def repeat_task(action, times):
    for _ in range(times):
        yield action

if __name__ == '__main__':
    task_to_repeat = "Hello"
    number_of_repeats = 10
    repeated_tasks = list(repeat_task(task_to_repeat, number_of_repeats))
    print(repeated_tasks)