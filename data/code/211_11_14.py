def set_operations(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference_set1 = set1.difference(set2)
    difference_set2 = set2.difference(set1)
    return intersection, union, difference_set1, difference_set2

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    result = set_operations(sample_set1, sample_set2)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("Difference (set1 - set2):", result[2])
    print("Difference (set2 - set1):", result[3])