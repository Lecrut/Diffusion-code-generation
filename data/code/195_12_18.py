def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if isinstance(list1[i], list) and isinstance(list2[i], list):
            if not compare_lists(list1[i], list2[i]):
                return False
        elif list1[i] != list2[i]:
            return False
    return True

if __name__ == '__main__':
    list_a = [1, 2, [3, 4]]
    list_b = [1, 2, [3, 4]]
    list_c = [1, 2, [3, 5]]
    print(f"Comparing {list_a} and {list_b}: {compare_lists(list_a, list_b)}")
    print(f"Comparing {list_a} and {list_c}: {compare_lists(list_a, list_c)}")