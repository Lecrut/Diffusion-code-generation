def find_first_mismatch(list1, list2):
    if len(list1) != len(list2):
        return [i for i in range(min(len(list1), len(list2)))]
    for index, (item1, item2) in enumerate(zip(list1, list2)):
        if item1 != item2:
            return [index]
    return []
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    list_c = [1, 2, 9, 4]
    print(find_first_mismatch(list_a, list_b))
    print(find_first_mismatch(list_a, list_c))