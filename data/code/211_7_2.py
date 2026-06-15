import numpy as np
def jaccard_index(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 1.0 if intersection == 0 else 0.0
    return intersection / union
if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    print(jaccard_index(sample_set1, sample_set2))
    sample_set3 = {10, 20, 30}
    sample_set4 = {30, 40, 50}
    print(jaccard_index(sample_set3, sample_set4))
    sample_set5 = {1, 2, 3}
    sample_set6 = {1, 2, 3}
    print(jaccard_index(sample_set5, sample_set6))
    sample_set7 = set()
    sample_set8 = set()
    print(jaccard_index(sample_set7, sample_set8))