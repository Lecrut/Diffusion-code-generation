def compare_sets(set1, set2):
    return max(set1, set2)

if __name__ == '__main__':
    sample_set1 = {3, 5, 8}
    sample_set2 = {4, 6, 9}
    print(compare_sets(sample_set1, sample_set2))