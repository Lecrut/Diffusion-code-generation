def set_operations(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets of integers.")
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference = set1.difference(set2)
    
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    
    intersection_result, union_result, difference_result = set_operations(sample_set1, sample_set2)
    
    print("Intersection:", intersection_result)
    print("Union:", union_result)
    print("Difference:", difference_result)