def is_float_in_list(target, float_list):
    return any(abs(target - item) < 1e-9 for item in float_list)

if __name__ == '__main__':
    sample_list = [0.1 + 0.2, 0.3, 0.4]
    target_value = 0.3
    print(is_float_in_list(target_value, sample_list))