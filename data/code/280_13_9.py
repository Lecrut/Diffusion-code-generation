class ActionRepeater:
    MAX_REPETITIONS = 5

    @staticmethod
    def perform_action(param):
        return f"Action performed with {param}"

    @classmethod
    def repeat_actions(cls, parameters):
        results = [cls.perform_action(p) for p in parameters]
        return results

if __name__ == '__main__':
    sample_params = ['a', 'b', 'c', 'd', 'e']
    repeated_results = ActionRepeater.repeat_actions(sample_params)
    print(repeated_results)