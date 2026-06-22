def repeat_task(action, times):
    for _ in range(times):
        yield action

if __name__ == '__main__':
    task_to_repeat = "Hello"
    number_of_repeats = 10
    result_generator = repeat_task(task_to_repeat, number_of_repeats)
    repeated_actions = list(result_generator)
    print(repeated_actions)