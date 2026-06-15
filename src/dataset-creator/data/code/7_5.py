def are_lists_equal(list1, list2):
    return list1 == list2
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = [3, 2, 1]
    list_d = [1, 2, 4]
    list_e = [1, 2]
    print(f"list_a == list_b: {are_lists_equal(list_a, list_b)}")
    print(f"list_a == list_c: {are_lists_equal(list_a, list_c)}")
    print(f"list_a == list_d: {are_lists_equal(list_a, list_d)}")
    print(f"list_a == list_e: {are_lists_equal(list_a, list_e)}")
    list_f = [1, 2, 3, 4]
    list_g = [1, 2, 3, 4]
    print(f"list_f == list_g: {are_lists_equal(list_f, list_g)}")