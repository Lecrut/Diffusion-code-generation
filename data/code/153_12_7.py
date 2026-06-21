def is_float_in_list(target, float_list):
    return any((abs(target - num) < 1e-09 for num in float_list))
if __name__ == '__main__':
    sample_list = [0.1 + i * 0.1 for i in range(10)]
    print(is_float_in_list(0.3, sample_list))
    print(is_float_in_list(0.4, sample_list))