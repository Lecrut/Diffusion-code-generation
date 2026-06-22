def repeat_action(action, times):
    if not isinstance(times, int) or times < 0:
        raise ValueError("times must be a non-negative integer")
    for _ in range(times):
        yield action

if __name__ == '__main__':
    action_to_repeat = "Hello"
    number_of_times = 10
    result_generator = repeat_action(action_to_repeat, number_of_times)
    repeated_actions = list(result_generator)
    print(repeated_actions)