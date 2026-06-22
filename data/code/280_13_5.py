class ActionRepeater:
    MAX_REPETITIONS = 5

    @staticmethod
    def perform_action(param):
        return f"Action performed with {param}"

if __name__ == '__main__':
    parameters = [10, 20, 30, 40, 50]
    results = [ActionRepeater.perform_action(p) for p in parameters]
    print(results)