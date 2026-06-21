def get_intersection(list1, list2):
    frozenset1 = frozenset(list1)
    frozenset2 = frozenset(list2)
    return list(frozenset1 & frozenset2)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result1 = get_intersection(list_a, list_b)
    print(f"Intersection of {list_a} and {list_b}: {result1}")