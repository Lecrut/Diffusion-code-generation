def bitwise_set_operations(set1, set2):
    intersection = set1 & set2
    union = set1 | set2
    difference = set1 - set2
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {True, False, True}
    sample_set2 = {False, False, True}
    result_intersection, result_union, result_difference = bitwise_set_operations(sample_set1, sample_set2)
    print("Intersection:", result_intersection)
    print("Union:", result_union)
    print("Difference:", result_difference)