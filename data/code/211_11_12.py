def set_operations(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets")
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference_set1_to_set2 = set1.difference(set2)
    difference_set2_to_set1 = set2.difference(set1)
    
    return {
        "intersection": intersection,
        "union": union,
        "difference_set1_to_set2": difference_set1_to_set2,
        "difference_set2_to_set1": difference_set2_to_set1
    }

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    result = set_operations(sample_set1, sample_set2)
    print("Intersection:", result["intersection"])
    print("Union:", result["union"])
    print("Difference (set1 - set2):", result["difference_set1_to_set2"])
    print("Difference (set2 - set1):", result["difference_set2_to_set1"])