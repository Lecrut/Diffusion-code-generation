def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection_set = set1.intersection(set2)
    return list(intersection_set)
if __name__ == '__main__':
    list_a = [1, 2, 2, 3, 4, 4]
    list_b = [2, 4, 4, 5, 6, 1]
    result = find_intersection(list_a, list_b)
    print(result)