def get_first_element(lst):
    first_element = None
    if lst:
        first_element = lst[0]
    return first_element

if __name__ == '__main__':
    test_list_1 = [7, 8, 9, 10]
    test_list_2 = []
    result_1 = get_first_element(test_list_1)
    result_2 = get_first_element(test_list_2)
    print(result_1)
    print(result_2)