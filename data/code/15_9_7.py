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
    list_c = list(range(1000000, 2000000))
    list_d = list(range(1000000))
    list_e = list(range(1000000))
    print(f"List A and List B identical: {are_lists_identical(list_a, list_b)}")
    print(f"List A and List C identical: {are_lists_identical(list_a, list_c)}")
    print(f"List D and List E identical: {are_lists_identical(list_d, list_e)}")
    print(f"List A and List D identical: {are_lists_identical(list_a, list_d)}")
    print(f"List A and List E identical: {are_lists_identical(list_a, list_e)}")