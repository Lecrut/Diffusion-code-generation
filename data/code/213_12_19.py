def set_operations(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference = set1.difference(set2)
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    
    result_intersection, result_union, result_difference = set_operations(sample_set1, sample_set2)
    
    print("Intersection:", result_intersection)
    print("Union:", result_union)
    print("Difference (Set1 - Set2):", result_difference)