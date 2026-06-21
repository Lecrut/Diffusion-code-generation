def set_operations(set1, set2):
    if not all(isinstance(x, int) for x in set1) or not all(isinstance(x, int) for x in set2):
        raise ValueError("Both sets must contain only integers.")
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference = set1.difference(set2)
    
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    result = set_operations(sample_set1, sample_set2)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("Difference:", result[2])