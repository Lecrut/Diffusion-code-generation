def compare_lists(list1, list2):
    return set(list1) == set(list2)

if __name__ == '__main__':
    LIST_A = [1, 2, 3, 4, 5]
    LIST_B = [1, 2, 3, 4, 5]
    LIST_C = [5, 4, 3, 2, 1]
    LIST_D = [1, 2, 3, 4, 6]
    LIST_E = [1, 2, 3, 4]

    print(f"Comparing {LIST_A} and {LIST_B}: {compare_lists(LIST_A, LIST_B)}")
    print(f"Comparing {LIST_A} and {LIST_C}: {compare_lists(LIST_A, LIST_C)}")
    print(f"Comparing {LIST_A} and {LIST_D}: {compare_lists(LIST_A, LIST_D)}")
    print(f"Comparing {LIST_A} and {LIST_E}: {compare_lists(LIST_A, LIST_E)}")