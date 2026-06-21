def intersect_with_bitwise(frozenset1, frozenset2):
    return frozenset1 & frozenset2

if __name__ == '__main__':
    sample_set1 = frozenset([1, 2, 3, 4])
    sample_set2 = frozenset([3, 4, 5, 6])
    result = intersect_with_bitwise(sample_set1, sample_set2)
    print(result)