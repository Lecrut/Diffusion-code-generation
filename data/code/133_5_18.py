def boolean_set_operations(set1, set2):
    intersection = set1 & set2
    union = set1 | set2
    difference1_to_2 = set1 - set2
    difference2_to_1 = set2 - set1
    return intersection, union, difference1_to_2, difference2_to_1

if __name__ == '__main__':
    sample_set1 = {True, False, True}
    sample_set2 = {False, False, True}
    result = boolean_set_operations(sample_set1, sample_set2)
    print(f"Intersection: {result[0]}")
    print(f"Union: {result[1]}")
    print(f"Difference (Set1 - Set2): {result[2]}")
    print(f"Difference (Set2 - Set1): {result[3]}")