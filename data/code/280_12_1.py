class Repeater:
    def repeat_action(self, action, times):
        for _ in range(times):
            yield action
if __name__ == '__main__':
    repeater = Repeater()
    action_to_repeat = "Hello"
    number_of_repeats = 5
    result_generator = repeater.repeat_action(action_to_repeat, number_of_repeats)
    repeated_actions = list(result_generator)
    print(repeated_actions)