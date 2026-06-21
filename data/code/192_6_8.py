def intersect_lists(list1, list2):
    return [item for item in list1 if item in list2 and isinstance(item, (int, str, float))]

if __name__ == '__main__':
    print(intersect_lists([1, 'a', 3.14, None], ['a', 2, 3.14]))