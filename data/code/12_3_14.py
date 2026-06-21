def get_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_middle_element(sample_list)
    print(result)

    sample_list_even = [1, 2, 3, 4]
    result_even = get_middle_element(sample_list_even)
    print(result_even)

    sample_list_single = [42]
    result_single = get_middle_element(sample_list_single)
    print(result_single)

    sample_list_empty = []
    result_empty = get_middle_element(sample_list_empty)
    print(result_empty)