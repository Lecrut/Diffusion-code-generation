def merge_and_sort_sets(set1, set2):
    if not all(isinstance(i, (int, float)) for i in set1.union(set2)):
        raise ValueError("Both sets should only contain numbers")
    return sorted(set1.union(set2))

if __name__ == '__main__':
    sample_set1 = {3, 1, 4}
    sample_set2 = {2, 5, 6}
    result = merge_and_sort_sets(sample_set1, sample_set2)
    print(result)