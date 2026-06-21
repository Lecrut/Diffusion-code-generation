def set_operations(set1, set2):
    if not all(isinstance(i, set) for i in [set1, set2]):
        raise ValueError("Inputs must be sets")
    union_result = set1.union(set2)
    intersection_result = set1.intersection(set2)
    symmetric_difference_result = set1.symmetric_difference(set2)
    return union_result, intersection_result, symmetric_difference_result

if __name__ == '__main__':
    sample_set_a = {'apple', 'banana', 'cherry'}
    sample_set_b = {'banana', 'grape', 'kiwi'}
    union, intersection, difference = set_operations(sample_set_a, sample_set_b)
    print(f"Sample Set A: {sample_set_a}")
    print(f"Sample Set B: {sample_set_b}")
    print(f"Union (A or B): {union}")
    print(f"Intersection (A and B): {intersection}")
    print(f"Symmetric Difference (A XOR B): {difference}")