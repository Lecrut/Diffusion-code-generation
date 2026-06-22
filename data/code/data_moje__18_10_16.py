def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [10, 20, 30, 40]
    sample_list_3 = [42]
    sample_list_4 = []

    print(get_middle_element(sample_list_1))
    print(get_middle_element(sample_list_2))
    print(get_middle_element(sample_list_3))
    print(get_middle_element(sample_list_4))