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
    print(f"List A and List B identical: {are_lists_identical(list_a, list_b)}")
    print(f"List A and List C identical: {are_lists_identical(list_a, list_c)}")
    print(f"List A and List D identical: {are_lists_identical(list_a, list_d)}")
    list_e = [1, 2, 3, 4]
    list_f = [1, 2, 3, 5]
    print(f"List E and List F identical: {are_lists_identical(list_e, list_f)}")
    list_g = [10, 20, 30]
    list_h = [10, 20, 30, 40]
    print(f"List G and List H identical: {are_lists_identical(list_g, list_h)}")