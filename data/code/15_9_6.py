import random
def are_lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
if __name__ == '__main__':
    list_a = list(range(1000000))
    list_b = list(range(1000000))
    list_c = list(range(1000000))
    list_d = list(range(1000001))
    print(f"A and B are identical: {are_lists_identical(list_a, list_b)}")
    print(f"A and C are identical: {are_lists_identical(list_a, list_c)}")
    print(f"A and D are identical: {are_lists_identical(list_a, list_d)}")
    list_e = [1, 2, 3, 4]
    list_f = [1, 2, 3, 5]
    list_g = [1, 2, 3, 4]
    print(f"E and F are identical: {are_lists_identical(list_e, list_f)}")
    print(f"E and G are identical: {are_lists_identical(list_e, list_g)}")
    list_h = [10, 20, 30]
    list_i = [10, 20, 30]
    list_j = [10, 20, 31]
    print(f"H and I are identical: {are_lists_identical(list_h, list_i)}")
    print(f"H and J are identical: {are_lists_identical(list_h, list_j)}")
    list_k = [1, 2]
    list_l = [1, 2, 3]
    print(f"K and L are identical: {are_lists_identical(list_k, list_l)}")