def intersect_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)
if __name__ == '__main__':
    result = intersect_lists([1, 2, 3, 4], [3, 4, 5, 6])
    print(result)