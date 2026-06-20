TRUE_VALUES = {'true', '1', 'yes'}
FALSE_VALUES = {'false', '0', 'no'}

def compare_sets(set1, set2):
    intersection = set1 & set2
    union = set1 | set2
    difference = set1 - set2
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {'true', 'False', '1'}
    sample_set2 = {'yes', '0', 'no', 'True'}
    result = compare_sets(sample_set1, sample_set2)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("Difference:", result[2])