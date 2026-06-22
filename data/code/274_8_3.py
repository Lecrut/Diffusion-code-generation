def print_until_condition(my_list, condition):
    index = 0
    while index < len(my_list) and not condition(my_list[index]):
        print(my_list[index])
        index += 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    condition = lambda x: x > 3
    print_until_condition(sample_list, condition)