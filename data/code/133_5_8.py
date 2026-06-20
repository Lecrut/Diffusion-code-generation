def set_operations(set1, set2):
    intersection = set1 & set2
    union = set1 | set2
    difference = set1 - set2
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {True, False}
    sample_set2 = {False, True, 0, 1}
    result = set_operations(sample_set1, sample_set2)
    print(result)