def is_float_in_list(target, float_list):
    return any((abs(target - item) < 1e-09 for item in float_list))
if __name__ == '__main__':
    sample_list = [0.1, 0.2, 0.3]
    print(is_float_in_list(0.20000000000000007, sample_list))
    print(is_float_in_list(0.4, sample_list))