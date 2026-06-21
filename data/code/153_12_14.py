def is_float_in_list(target, float_list):
    if not isinstance(target, (int, float)) or not all(isinstance(num, (int, float)) for num in float_list):
        raise ValueError("Target and list elements must be numbers.")
    
    return any(abs(target - num) < 1e-9 for num in float_list)

if __name__ == '__main__':
    sample_list = [0.1 + 0.2, 0.3, 0.4]
    target_value = 0.5
    result = is_float_in_list(target_value, sample_list)
    print(result)