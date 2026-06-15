def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            return False
    return True
if __name__ == '__main__':
    list_a = [1, 3, 5]
    list_b = [1, 4, 6]
    result1 = compare_lists(list_a, list_b)
    print(f"Result 1: {result1}")
    list_c = [10, 20]
    list_d = [5, 15]
    result2 = compare_lists(list_c, list_d)
    print(f"Result 2: {result2}")
    list_e = [1, 2, 3]
    list_f = [1, 2, 1]
    result3 = compare_lists(list_e, list_f)
    print(f"Result 3: {result3}")
    list_g = [5, 5]
    list_h = [5, 5]
    result4 = compare_lists(list_g, list_h)
    print(f"Result 4: {result4}")