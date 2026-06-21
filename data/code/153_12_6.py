def float_in_list(target, lst):
    return any((abs(target - item) < 1e-09 for item in lst))
if __name__ == '__main__':
    sample_list = [0.1 + 0.2, 0.3, 0.4]
    print(float_in_list(0.3, sample_list))
    print(float_in_list(0.5, sample_list))