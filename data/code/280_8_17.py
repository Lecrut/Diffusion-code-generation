class ActionRepeater:
    MAX_REPETITIONS = 10

    @staticmethod
    def repeat_action(times):
        if times == 0:
            return []
        else:
            action_result = f"Action {times}"
            return [action_result] + ActionRepeater.repeat_action(times - 1)

if __name__ == '__main__':
    sample_values = ActionRepeater.MAX_REPETITIONS
    final_result = ActionRepeater.repeat_action(sample_values)
    print(final_result)