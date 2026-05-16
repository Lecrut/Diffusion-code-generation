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
    list_d = [1, 2, 3, 4]
    list_e = [1, 2, 3, 4]
    list_f = [1, 2, 3, 5]
    print(f"Test 4 (Small identical): {are_lists_identical(list_d, list_e)}")
    print(f"Test 5 (Small different): {are_lists_identical(list_d, list_f)}")
    list_g = [1] * 1000000
    list_h = [1] * 1000000
    list_i = [2] * 1000000
    print(f"Test 6 (Large identical): {are_lists_identical(list_g, list_h)}")
    print(f"Test 7 (Large different): {are_lists_identical(list_g, list_i)}")