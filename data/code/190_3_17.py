def float_exists(lst, target):
    return any(abs(x - target) < 1e-9 for x in lst)

if __name__ == '__main__':
    sample_list = [3.14159, 2.71828, 1.61803]
    target_number = 3.14
    print(float_exists(sample_list, target_number))