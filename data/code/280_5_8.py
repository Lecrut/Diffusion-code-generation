class ActionRepeater:
    DEFAULT_REPETITIONS = 10

    @staticmethod
    def repeat_action(action):
        return [action() for _ in range(ActionRepeater.DEFAULT_REPETITIONS)]

if __name__ == '__main__':
    action_result = ActionRepeater.repeat_action(lambda: "Action")
    print(action_result)