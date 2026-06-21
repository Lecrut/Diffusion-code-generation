def is_float_in_list(target, float_list):
    tolerance = 1e-9
    for num in float_list:
        if abs(target - num) < tolerance:
            return True
    return False

if __name__ == '__main__':
    sample_list = [0.3333333333333333, 0.6666666666666666, 1.0]
    target_value_1 = 0.5
    target_value_2 = 0.75
    result_1 = is_float_in_list(target_value_1, sample_list)
    result_2 = is_float_in_list(target_value_2, sample_list)
    print(f"List: {sample_list}")
    print(f"Does the list contain {target_value_1}? {result_1}")
    print(f"Does the list contain {target_value_2}? {result_2}")