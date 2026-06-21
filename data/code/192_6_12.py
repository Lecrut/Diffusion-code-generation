def intersect_lists(l1, l2):
    return [item for item in l1 if item in l2 and isinstance(item, (int, str, float))]

if __name__ == '__main__':
    list1 = [1, 'a', 3.14, None, True]
    list2 = ['b', 1, 3.14, False]
    print(intersect_lists(list1, list2))