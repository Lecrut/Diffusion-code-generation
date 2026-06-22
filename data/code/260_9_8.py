def merge_and_sort_sets(set1, set2):
    return sorted(set1.union(set2))

if __name__ == '__main__':
    sample_set1 = {3, 5, 8, 10}
    sample_set2 = {2, 4, 6, 8}
    result = merge_and_sort_sets(sample_set1, sample_set2)
    print(result)