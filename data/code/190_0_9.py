def integer_exists(integer_list, target):
    return target in set(integer_list)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_integer = 30
    print(integer_exists(sample_list, target_integer))