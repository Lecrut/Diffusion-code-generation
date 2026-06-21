def float_exists(lst, target):
    return any(abs(x - target) < 1e-9 for x in lst)

if __name__ == '__main__':
    sample_list = [3.14, 2.718, 0.577, 1.618]
    target_number = 2.718
    print(float_exists(sample_list, target_number))