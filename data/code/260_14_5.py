def compare_sets(set1, set2):
    return set1 if sum(set1) > sum(set2) else set2

if __name__ == '__main__':
    sample_set1 = {3, 5, 7}
    sample_set2 = {1, 4, 6}
    print(compare_sets(sample_set1, sample_set2))