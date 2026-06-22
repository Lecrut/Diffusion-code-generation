def repeat_action(times, result_list):
    if times < 0:
        raise ValueError("Times must be non-negative")
    if times == 0:
        return result_list
    action_result = f"Action {times}"
    result_list.append(action_result)
    return repeat_action(times - 1, result_list)

if __name__ == '__main__':
    sample_values = []
    final_result = repeat_action(10, sample_values)
    print(final_result)