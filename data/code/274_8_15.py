def print_list_until_condition(data_list, condition):
    index = 0
    while index < len(data_list) and not condition(data_list[index]):
        print(data_list[index])
        index += 1

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    condition = lambda x: isinstance(x, str)
    print_list_until_condition(sample_list, condition)