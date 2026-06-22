class Repeater:
    MAX_REPETITIONS = 10

    @staticmethod
    def repeat_action(action):
        return action * Repeater.MAX_REPETITIONS

if __name__ == '__main__':
    repeater_instance = Repeater()
    action_to_repeat = "Hello"
    repeated_actions = repeater_instance.repeat_action(action_to_repeat)
    print(repeated_actions)