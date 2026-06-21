def validate_sets(set1, set2):
    if not all(isinstance(item, int) for item in set1 | set2):
        raise ValueError("Both sets must contain only integers.")
    return True

def set_operations(set1, set2):
    validate_sets(set1, set2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference = set1.difference(set2)
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    result = set_operations(sample_set1, sample_set2)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("Difference (set1 - set2):", result[2])