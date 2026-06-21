def set_operations(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    symmetric_difference = set1.symmetric_difference(set2)
    return intersection, union, symmetric_difference

if __name__ == '__main__':
    sample_set_a = {'apple', 'banana', 'cherry'}
    sample_set_b = {'banana', 'cherry', 'date'}
    intersection_result, union_result, symmetric_diff_result = set_operations(sample_set_a, sample_set_b)
    print(f"Sample Set A: {sample_set_a}")
    print(f"Sample Set B: {sample_set_b}")
    print(f"Intersection (A and B): {intersection_result}")
    print(f"Union (A or B): {union_result}")
    print(f"Symmetric Difference (A ⊕ B): {symmetric_diff_result}")