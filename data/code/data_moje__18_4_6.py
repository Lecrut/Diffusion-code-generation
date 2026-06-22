def get_middle_value(lst):
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    odd_length = [1, 2, 3, 4, 5]
    even_length = [10, 20, 30, 40]
    single_element = [99]
    five_elements = [1, 2, 3, 4, 5, 6, 7]

    print(get_middle_value(odd_length))
    print(get_middle_value(even_length))
    print(get_middle_value(single_element))
    print(get_middle_value(five_elements))