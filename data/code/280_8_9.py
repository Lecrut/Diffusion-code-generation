def repeat_action(n, result_list):
    if n == 0:
        return result_list
    else:
        action_result = f"Action {n}"
        result_list.append(action_result)
        return repeat_action(n - 1, result_list)

if __name__ == '__main__':
    sample_values = []
    final_result = repeat_action(10, sample_values)
    print(final_result)