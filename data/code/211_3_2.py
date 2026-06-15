def compare_sets(set1, set2):
    result1 = set1.intersection(set2)
    result2 = set1.union(set2)
    return result1, result2
if __name__ == '__main__':
    sample_set_a = {1, 2, 3, 4, 5}
    sample_set_b = {4, 5, 6, 7, 8}
    intersection_result, union_result = compare_sets(sample_set_a, sample_set_b)
    print(f"Set A: {sample_set_a}")
    print(f"Set B: {sample_set_b}")
    print(f"Intersection (A and B): {intersection_result}")
    print(f"Union (A or B): {union_result}")