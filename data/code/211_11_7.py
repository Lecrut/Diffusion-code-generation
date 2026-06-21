def set_operations(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference = set1.difference(set2)
    return {
        "intersection": intersection,
        "union": union,
        "difference": difference
    }

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    result = set_operations(sample_set1, sample_set2)
    print("Intersection:", result["intersection"])
    print("Union:", result["union"])
    print("Difference (set1 - set2):", result["difference"])