def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for a, b in zip(list1, list2):
        if not (a <= b):
            return False
    return True
if __name__ == '__main__':
    list_a = [1, 3, 5]
    list_b = [1, 4, 6]
    result1 = compare_lists(list_a, list_b)
    print(f"Result 1: {result1}")
    list_c = [2, 3, 7]
    list_d = [1, 4, 6]
    result2 = compare_lists(list_c, list_d)
    print(f"Result 2: {result2}")
    list_e = [10, 20]
    list_f = [5, 15]
    result3 = compare_lists(list_e, list_f)
    print(f"Result 3: {result3}")
    list_g = [1, 2]
    list_h = [1, 2, 3]
    result4 = compare_lists(list_g, list_h)
    print(f"Result 4: {result4}")