def repeater(action, times):
    for _ in range(times):
        yield action
class Repeater:
    def repeat_action(self, action, times):
        return repeater(action, times)
if __name__ == '__main__':
    my_repeater = Repeater()
    action_to_repeat = "Hello"
    number_of_times = 3
    result_generator = my_repeater.repeat_action(action_to_repeat, number_of_times)
    repeated_actions = list(result_generator)
    print(repeated_actions)