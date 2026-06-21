def check_integer_exists(large_list, target):
    return target in large_list

if __name__ == '__main__':
    sample_list = list(range(1000000))
    target_value = 500000
    print(check_integer_exists(sample_list, target_value))