def integer_exists(integer_list, target):
    return target in set(integer_list)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_integer = 3
    print(integer_exists(sample_list, target_integer))