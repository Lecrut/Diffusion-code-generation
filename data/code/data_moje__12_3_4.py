def get_middle_element(data):
    if not data:
        return None
    mid_index = len(data) // 2
    return data[mid_index]

if __name__ == '__main__':
    test_list_1 = [1, 2, 3, 4, 5]
    test_list_2 = [10, 20, 30, 40]
    test_list_3 = []
    test_list_4 = [42]

    print(get_middle_element(test_list_1))
    print(get_middle_element(test_list_2))
    print(get_middle_element(test_list_3))
    print(get_middle_element(test_list_4))