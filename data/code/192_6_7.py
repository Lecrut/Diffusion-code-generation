def intersect_lists(list1, list2):
    return [item for item in list1 if item in list2 and isinstance(item, (int, float, str, tuple))]

if __name__ == '__main__':
    print(intersect_lists([1, 'a', 3.14, (1, 2)], ['b', 3.14, 5, (1, 2)]))