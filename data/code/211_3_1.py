def compare_sets(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference1 = set1.difference(set2)
    difference2 = set2.difference(set1)
    return intersection, union, difference1, difference2
if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5, 6}
    sample_set2 = {4, 5, 6, 7, 8, 9}
    intersection_result, union_result, diff1_result, diff2_result = compare_sets(sample_set1, sample_set2)
    print(f"Set 1: {sample_set1}")
    print(f"Set 2: {sample_set2}")
    print(f"Intersection: {intersection_result}")
    print(f"Union: {union_result}")
    print(f"Difference (Set 1 - Set 2): {diff1_result}")
    print(f"Difference (Set 2 - Set 1): {diff2_result}")