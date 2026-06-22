def print_until_value(my_list, target):
    index = 0
    while index < len(my_list) and my_list[index] != target:
        print(my_list[index])
        index += 1

if __name__ == '__main__':
    sample_list = [10, "world", 3.14, True, "hello"]
    target_value = "hello"
    print_until_value(sample_list, target_value)