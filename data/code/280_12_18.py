def repeat_action(action, times):
    for _ in range(times):
        print(action)

if __name__ == '__main__':
    action_to_repeat = "Hello"
    number_of_times = 10
    repeat_action(action_to_repeat, number_of_times)