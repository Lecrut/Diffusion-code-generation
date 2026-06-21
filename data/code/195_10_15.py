def are_lists_identical(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError('Both inputs must be lists.')
    return set(list1) == set(list2)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 3, 4, 5]
    list_c = [5, 4, 3, 2, 1]
    list_d = [1, 2, 3, 4, 6]
    list_e = 'hello'
    print(f'Comparing {list_a} and {list_b}: {are_lists_identical(list_a, list_b)}')
    print(f'Comparing {list_a} and {list_c}: {are_lists_identical(list_a, list_c)}')
    print(f'Comparing {list_a} and {list_d}: {are_lists_identical(list_a, list_d)}')