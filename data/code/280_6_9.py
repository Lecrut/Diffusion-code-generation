class ActionRepeater:
    MAX_REPETITIONS = 3

    @staticmethod
    def repeat_action():
        phrase = "Action repeated"
        for _ in range(ActionRepeater.MAX_REPETITIONS):
            print(phrase)
            if _ == ActionRepeater.MAX_REPETITIONS - 1:
                break

if __name__ == '__main__':
    ActionRepeater.repeat_action()