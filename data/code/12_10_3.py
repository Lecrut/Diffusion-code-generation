def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [1, 2, 3, 4, 5, 6]
    sample_list_empty = []

    result_odd = get_middle_element(sample_list_odd)
    result_even = get_middle_element(sample_list_even)
    result_empty = get_middle_element(sample_list_empty)

    print(result_odd)
    print(result_even)
    print(result_empty)