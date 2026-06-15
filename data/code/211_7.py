import itertools
def jaccard_index(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if not union:
        return 1.0 if not set1 and not set2 else 0.0
    return len(intersection) / len(union)
if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    print(jaccard_index(sample_set1, sample_set2))
    sample_set3 = {'a', 'b', 'c'}
    sample_set4 = {'c', 'd', 'e'}
    print(jaccard_index(sample_set3, sample_set4))
    sample_set5 = {10, 20}
    sample_set6 = {30, 40}
    print(jaccard_index(sample_set5, sample_set6))
    sample_set7 = {1, 2}
    sample_set8 = {1, 2}
    print(jaccard_index(sample_set7, sample_set8))
    sample_set9 = set()
    sample_set10 = set()
    print(jaccard_index(sample_set9, sample_set10))