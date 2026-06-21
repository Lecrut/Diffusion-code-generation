def get_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    test_list_1 = [10, 20, 30, 40, 50]
    print(get_middle_element(test_list_1))
    test_list_2 = [1, 2, 3, 4]
    print(get_middle_element(test_list_2))
    test_list_3 = ['a', 'b', 'c']
    print(get_middle_element(test_list_3))
    test_list_4 = []
    print(get_middle_element(test_list_4))