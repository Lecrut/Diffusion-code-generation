def is_float_in_list(target, float_list):
    epsilon = 1e-9
    for num in float_list:
        if abs(target - num) < epsilon:
            return True
    return False

if __name__ == '__main__':
    sample_list = [0.1 + 0.2, 0.3, 0.4]
    target_value = 0.5
    print(is_float_in_list(target_value, sample_list))