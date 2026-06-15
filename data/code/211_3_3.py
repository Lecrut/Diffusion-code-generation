def compare_sets(set1, set2):
    result1 = set1.intersection(set2)
    result2 = set1.union(set2)
    return result1, result2
if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    intersection_result, union_result = compare_sets(sample_set1, sample_set2)
    print(f"Sample Set 1: {sample_set1}")
    print(f"Sample Set 2: {sample_set2}")
    print(f"Intersection (Set1 and Set2): {intersection_result}")
    print(f"Union (Set1 or Set2): {union_result}")