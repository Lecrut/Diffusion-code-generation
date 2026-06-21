def float_exists(float_list, target):
    return target in float_list

if __name__ == '__main__':
    sample_floats = [3.14, 2.71, 0.577, 1.618]
    target_number = 2.71
    print(float_exists(sample_floats, target_number))