class ActionRepeater:
    DEFAULT_ITERATIONS = 10

    @staticmethod
    def repeat_action(times=DEFAULT_ITERATIONS):
        for i in range(times):
            print(f"Iteration {i + 1}")

if __name__ == '__main__':
    ActionRepeater.repeat_action()