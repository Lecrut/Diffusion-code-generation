class ActionRepeater:
    MAX_REPETITIONS = 10

    @staticmethod
    def repeat_action(action):
        return [action() for _ in range(ActionRepeater.MAX_REPETITIONS)]

if __name__ == '__main__':
    result = ActionRepeater.repeat_action(lambda: "Hello, World!")
    print(result)