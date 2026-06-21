def get_intersection(list1, list2):
    set1 = frozenset(list1)
    set2 = frozenset(list2)
    return list(set1 & set2)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result1 = get_intersection(list_a, list_b)
    print(f"Intersection of {list_a} and {list_b}: {result1}")
    list_c = ['a', 'b', 'c', 'd']
    list_d = ['c', 'd', 'e', 'f']
    result2 = get_intersection(list_c, list_d)
    print(f"Intersection of {list_c} and {list_d}: {result2}")