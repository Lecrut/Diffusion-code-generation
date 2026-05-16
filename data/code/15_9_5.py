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
    list_e = list(range(1000000))
    print(f"A and B identical: {are_lists_identical(list_a, list_b)}")
    print(f"A and C identical: {are_lists_identical(list_a, list_c)}")
    print(f"A and D identical: {are_lists_identical(list_a, list_d)}")
    print(f"A and E identical: {are_lists_identical(list_a, list_e)}")
    list_f = [1, 2, 3]
    list_g = [1, 2, 4]
    print(f"F and G identical: {are_lists_identical(list_f, list_g)}")
    list_h = [1, 2, 3, 4]
    list_i = [1, 2, 3, 4, 5]
    print(f"H and I identical: {are_lists_identical(list_h, list_i)}")