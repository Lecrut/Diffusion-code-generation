def validate_sets(set1, set2):
    if not all(isinstance(item, bool) for item in set1) or not all(isinstance(item, bool) for item in set2):
        raise ValueError("Both sets must contain only boolean values.")

def bitwise_operations(set1, set2):
    intersection = set1 & set2
    union = set1 | set2
    difference_set1 = set1 - set2
    return intersection, union, difference_set1

if __name__ == '__main__':
    sample_set1 = {True, False, True}
    sample_set2 = {False, True}
    
    validate_sets(sample_set1, sample_set2)
    
    result_intersection, result_union, result_difference = bitwise_operations(sample_set1, sample_set2)
    
    print("Intersection:", result_intersection)
    print("Union:", result_union)
    print("Difference (Set1 - Set2):", result_difference)