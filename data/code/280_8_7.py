def repeat_action(times):
    if times < 0:
        raise ValueError("Number of repetitions must be non-negative")
    
    result = []
    def helper(current_times, current_result):
        if current_times == 0:
            return current_result
        else:
            action_result = f"Action {current_times}"
            current_result.append(action_result)
            return helper(current_times - 1, current_result)
    
    return helper(times, result)

if __name__ == '__main__':
    sample_values = []
    final_result = repeat_action(10)
    print(final_result)