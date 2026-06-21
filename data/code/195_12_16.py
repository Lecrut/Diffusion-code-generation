def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if isinstance(item1, list) and isinstance(item2, list):
            if not compare_lists(item1, item2):
                return False
        elif item1 != item2:
            return False
    return True
if __name__ == '__main__':
    list_a = [1, 2, 2, [3, 4]]
    list_b = [[3, 4], 2, 1, 2]
    list_c = [1, 2, 2, 4]
    list_d = [1, 2, 2]
    print(f'Comparing {list_a} and {list_b}: {compare_lists(list_a, list_b)}')
    print(f'Comparing {list_a} and {list_c}: {compare_lists(list_a, list_c)}')
    print(f'Comparing {list_d} and {list_e}: {compare_lists(list_d, list_e)}')