def set_operations(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference = set1.difference(set2)
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {10, 20, 30, 40}
    sample_set2 = {30, 40, 50, 60}
    result = set_operations(sample_set1, sample_set2)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("Difference (set1 - set2):", result[2])