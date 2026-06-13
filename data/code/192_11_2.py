def find_intersection(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    intersection = set_a.intersection(set_b)
    return list(intersection)
if __name__ == '__main__':
    list1 = [1, 2, 2, 3, 4, 4]
    list2 = [3, 4, 4, 5, 6]
    result = find_intersection(list1, list2)
    print(result)