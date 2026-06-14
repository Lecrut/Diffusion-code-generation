def compare_sets(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    unique_a = set_a - set_b
    unique_b = set_b - set_a
    return {
        "intersection_size": len(intersection),
        "union_size": len(union),
        "unique_to_a": unique_a,
        "unique_to_b": unique_b
    }
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    result = compare_sets(list1, list2)
    print(result)