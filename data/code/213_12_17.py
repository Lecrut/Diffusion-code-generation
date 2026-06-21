def set_operations(set1, set2):
    intersection = set1 & set2
    union = set1 | set2
    difference = set1 - set2
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    result = set_operations(sample_set1, sample_set2)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("Difference (set1 - set2):", result[2])