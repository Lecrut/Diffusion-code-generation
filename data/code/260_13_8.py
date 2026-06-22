def is_subset(set1, set2):
    return set1 <= set2

if __name__ == '__main__':
    sample_set1 = {1, 3, 5}
    sample_set2 = {1, 2, 3, 4, 5, 6}
    result = is_subset(sample_set1, sample_set2)
    print(result)