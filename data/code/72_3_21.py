def compare_and_print_greater(list_first, list_second):
    length = min(len(list_first), len(list_second))
    index = 0
    while index < length:
        current_first = list_first[index]
        current_second = list_second[index]
        if current_first > current_second:
            print(f"{current_first} > {current_second}")
        index += 1

if __name__ == '__main__':
    data_x = [20, 15, 25, 10]
    data_y = [10, 16, 20, 12]
    compare_and_print_greater(data_x, data_y)