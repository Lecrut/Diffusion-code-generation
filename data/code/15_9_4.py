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
    print(f"Test 1 (Identical): {are_lists_identical(list_a, list_b)}")
    print(f"Test 2 (Different content): {are_lists_identical(list_a, list_c)}")
    print(f"Test 3 (Different length): {are_lists_identical(list_a, list_b[:999999])}")
    list_d = [1, 2, 3]
    list_e = [1, 2, 4]
    print(f"Test 4 (Small different): {are_lists_identical(list_d, list_e)}")
    list_f = [10]
    list_g = [10, 20]
    print(f"Test 5 (Different length): {are_lists_identical(list_f, list_g)}")
    list_h = [1] * 1000000
    list_i = [1] * 1000000
    print(f"Test 6 (Large identical): {are_lists_identical(list_h, list_i)}")
    list_j = [1] * 999999 + [2]
    list_k = [1] * 1000000
    print(f"Test 7 (Large different): {are_lists_identical(list_j, list_k)}")