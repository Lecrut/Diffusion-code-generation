def get_middle_value(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [2, 4, 6, 8]
    single_element = [42]
    empty_list = []

    print(get_middle_value(odd_list))
    print(get_middle_value(even_list))
    print(get_middle_value(single_element))
    print(get_middle_value(empty_list))