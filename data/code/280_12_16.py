def repeat_task(action, times):
    for _ in range(times):
        yield action

if __name__ == '__main__':
    action_to_repeat = "Hello"
    number_of_times = 10
    result_generator = repeat_task(action_to_repeat, number_of_times)
    repeated_actions = list(result_generator)
    print(repeated_actions)