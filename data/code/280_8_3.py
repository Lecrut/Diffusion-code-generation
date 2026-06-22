def repeat_action(times):
    if times == 0:
        return []
    else:
        action_result = f"Action {times}"
        return [action_result] + repeat_action(times - 1)

if __name__ == '__main__':
    sample_values = []
    final_result = repeat_action(10)
    print(final_result)