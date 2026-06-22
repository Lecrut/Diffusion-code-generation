def print_until_number(my_list):
    index = 0
    while index < len(my_list) and not isinstance(my_list[index], int):
        print(my_list[index])
        index += 1

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True, "world"]
    print_until_number(sample_list)