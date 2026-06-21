INTERSECTION_THRESHOLD = 10

def fast_intersection(list1, list2):
    if len(list1) < INTERSECTION_THRESHOLD:
        set1 = frozenset(list1)
        set2 = frozenset(list2)
        return list(set1 & set2)
    else:
        set1 = frozenset(list2)
        set2 = frozenset(list1)
        return list(set1 & set2)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5]
    sample_list_b = [4, 5, 6, 7, 8]
    result = fast_intersection(sample_list_a, sample_list_b)
    print(f"Intersection of {sample_list_a} and {sample_list_b}: {result}")