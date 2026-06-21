def set_operations(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets.")
    
    intersection_result = set1.intersection(set2)
    union_result = set1.union(set2)
    symmetric_difference_result = set1.symmetric_difference(set2)
    
    return intersection_result, union_result, symmetric_difference_result

if __name__ == '__main__':
    sample_set_a = {'apple', 'banana', 'cherry'}
    sample_set_b = {'banana', 'cherry', 'date'}
    result = set_operations(sample_set_a, sample_set_b)
    print(f"Sample Set A: {sample_set_a}")
    print(f"Sample Set B: {sample_set_b}")
    print(f"Intersection (A and B): {result[0]}")
    print(f"Union (A or B): {result[1]}")
    print(f"Symmetric Difference (A ^ B): {result[2]}")