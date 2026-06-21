def integer_exists(num_list, target):
    num_set = set(num_list)
    return target in num_set

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_number = 3
    print(integer_exists(sample_list, target_number))