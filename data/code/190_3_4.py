def float_exists(lst, target):
    return any(abs(num - target) < 1e-9 for num in lst)

if __name__ == '__main__':
    sample_list = [1.0, 2.5, 3.7, 4.8]
    target_float = 2.5
    print(float_exists(sample_list, target_float))