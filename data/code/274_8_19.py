def print_until_condition(my_list, condition):
    index = 0
    while index < len(my_list) and not condition(my_list[index]):
        print(my_list[index])
        index += 1

if __name__ == '__main__':
    sample_list = [10, 20, "hello", True, 3.14]
    condition = lambda x: isinstance(x, str)
    print_until_condition(sample_list, condition)