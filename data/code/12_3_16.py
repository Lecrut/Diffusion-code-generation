def get_middle_element(lst):
    if not lst:
        return None
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_middle_element(sample_list)
    print(result)

    odd_length_list = [10, 20, 30, 40, 50, 60, 70]
    result_odd = get_middle_element(odd_length_list)
    print(result_odd)

    even_length_list = [1, 2, 3, 4]
    result_even = get_middle_element(even_length_list)
    print(result_even)

    single_element_list = [42]
    result_single = get_middle_element(single_element_list)
    print(result_single)

    empty_list = []
    result_empty = get_middle_element(empty_list)
    print(result_empty)