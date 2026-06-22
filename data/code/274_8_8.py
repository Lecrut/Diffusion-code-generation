def print_until_value(data_list, target_value):
    index = 0
    while index < len(data_list) and data_list[index] != target_value:
        print(data_list[index])
        index += 1

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    target = 3.14
    print_until_value(sample_list, target)