def set_operations(set1, set2):
    intersection = set1 & set2
    union = set1 | set2
    difference1 = set1 - set2
    difference2 = set2 - set1
    return intersection, union, difference1, difference2

if __name__ == '__main__':
    sample_set1 = {True, False, True}
    sample_set2 = {False, False, True}
    result = set_operations(sample_set1, sample_set2)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("Difference (set1 - set2):", result[2])
    print("Difference (set2 - set1):", result[3])