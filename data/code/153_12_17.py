def is_float_in_list(target, float_list):
    return any(abs(target - num) < 1e-9 for num in float_list)

if __name__ == '__main__':
    sample_list = [0.1 + 0.2, 0.3, 0.4]
    target_value_1 = 0.5
    target_value_2 = 0.6
    print(f"Does the list contain {target_value_1}? {is_float_in_list(target_value_1, sample_list)}")
    print(f"Does the list contain {target_value_2}? {is_float_in_list(target_value_2, sample_list)}")