def compare_sets(set1, set2):
    return max(set1, set2, key=len)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3}
    sample_set2 = {4, 5, 6, 7}
    print(compare_sets(sample_set1, sample_set2))