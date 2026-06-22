def get_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    print(get_middle_element(sample_list_1))

    sample_list_2 = [10, 20, 30, 40]
    print(get_middle_element(sample_list_2))

    sample_list_3 = [42]
    print(get_middle_element(sample_list_3))

    sample_list_4 = []
    print(get_middle_element(sample_list_4))