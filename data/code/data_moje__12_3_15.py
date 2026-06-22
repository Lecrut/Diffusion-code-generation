def get_middle_element(lst):
    length = len(lst)
    if length == 0:
        return None
    middle_index = length // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_list)
    print(result)

    sample_list_even = [10, 20, 30, 40]
    result_even = get_middle_element(sample_list_even)
    print(result_even)

    empty_list = []
    result_empty = get_middle_element(empty_list)
    print(result_empty)