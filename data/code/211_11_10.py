def validate_sets(set_a, set_b):
    if not all(isinstance(item, int) for item in set_a | set_b):
        raise ValueError("Both sets must contain only integers.")
    return set_a, set_b

def calculate_operations(set_a, set_b):
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    difference_ab = set_a - set_b
    difference_ba = set_b - set_a
    return {
        "intersection": intersection,
        "union": union,
        "unique_to_set_a": difference_ab,
        "unique_to_set_b": difference_ba
    }

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    validated_sets = validate_sets(sample_set1, sample_set2)
    result = calculate_operations(*validated_sets)
    print("Intersection:", result["intersection"])
    print("Union:", result["union"])
    print("Unique to set A:", result["unique_to_set_a"])
    print("Unique to set B:", result["unique_to_set_b"])