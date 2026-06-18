def are_lists_equal(list1, list2):
    return list1 == list2
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = [3, 2, 1]
    list_d = [1, 2]
    list_e = [1, 2, 3, 4]
    print(f"list_a == list_b: {are_lists_equal(list_a, list_b)}")
    print(f"list_a == list_c: {are_lists_equal(list_a, list_c)}")
    print(f"list_d == list_a: {are_lists_equal(list_d, list_a)}")
    print(f"list_e == list_a: {are_lists_equal(list_e, list_a)}")