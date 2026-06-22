class ActionRepeater:
    MAX_ITERATIONS = 10

    @staticmethod
    def repeat_action():
        for i in range(ActionRepeater.MAX_ITERATIONS):
            print(f"Iteration {i + 1}")

if __name__ == '__main__':
    ActionRepeater.repeat_action()