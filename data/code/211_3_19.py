def compare_sets(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both arguments must be sets.")
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    symmetric_difference = set1.symmetric_difference(set2)
    
    return intersection, union, symmetric_difference

if __name__ == '__main__':
    sample_set_a = {"apple", "banana", "cherry"}
    sample_set_b = {"banana", "cherry", "date"}
    
    try:
        intersection_result, union_result, sym_diff_result = compare_sets(sample_set_a, sample_set_b)
        print(f"Set A: {sample_set_a}")
        print(f"Set B: {sample_set_b}")
        print(f"Intersection (A and B): {intersection_result}")
        print(f"Union (A or B): {union_result}")
        print(f"Symmetric Difference (A ^ B): {sym_diff_result}")
    except ValueError as e:
        print(e)