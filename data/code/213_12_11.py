def validate_sets(set1, set2):
    if not all(isinstance(x, int) for x in set1):
        raise ValueError("Set 1 must contain only integers")
    if not all(isinstance(x, int) for x in set2):
        raise ValueError("Set 2 must contain only integers")

def calculate_intersection(set1, set2):
    validate_sets(set1, set2)
    return set1.intersection(set2)

def calculate_union(set1, set2):
    validate_sets(set1, set2)
    return set1.union(set2)

def calculate_difference(set1, set2):
    validate_sets(set1, set2)
    return set1.difference(set2)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}

    intersection = calculate_intersection(sample_set1, sample_set2)
    union = calculate_union(sample_set1, sample_set2)
    difference = calculate_difference(sample_set1, sample_set2)

    print("Intersection:", intersection)
    print("Union:", union)
    print("Difference:", difference)