def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    test_list_odd = [1, 3, 5, 7, 9]
    test_list_even = [10, 20, 30, 40]
    test_list_empty = []
    print(get_middle_element(test_list_odd))
    print(get_middle_element(test_list_even))
    print(get_middle_element(test_list_empty))