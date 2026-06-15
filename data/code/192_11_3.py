def find_intersection(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    intersection_set = set_a.intersection(set_b)
    return list(intersection_set)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 2, 5]
    list2 = [4, 5, 6, 7, 2, 8]
    result = find_intersection(list1, list2)
    print(result)