def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

if __name__ == '__main__':
    list_a = [1, 2, 2, 3, 4]
    list_b = [2, 1, 4, 3, 2]
    common_elements = find_common_elements(list_a, list_b)
    print(f"Common elements: {common_elements}")