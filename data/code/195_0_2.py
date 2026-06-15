def compare_lists(list1, list2):
    n = min(len(list1), len(list2))
    for i in range(n):
        if list1[i] != list2[i]:
            return i
    if len(list1) != len(list2):
        return -1
    return -1
if __name__ == '__main__':
    list_a = [1, 5, 3, 7, 9]
    list_b = [1, 5, 4, 7, 9]
    result1 = compare_lists(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    if result1 != -1:
        print(f"First difference found at index: {result1}")
    else:
        print("Lists are identical up to the length of the shorter list.")
    list_c = [1, 2, 3]
    list_d = [1, 2, 3, 4]
    result2 = compare_lists(list_c, list_d)
    print(f"\nList C: {list_c}")
    print(f"List D: {list_d}")
    if result2 != -1:
        print(f"First difference found at index: {result2}")
    else:
        print("Lists are identical up to the length of the shorter list.")
    list_e = [10, 20]
    list_f = [10, 20]
    result3 = compare_lists(list_e, list_f)
    print(f"\nList E: {list_e}")
    print(f"List F: {list_f}")
    if result3 != -1:
        print(f"First difference found at index: {result3}")
    else:
        print("Lists are identical up to the length of the shorter list.")