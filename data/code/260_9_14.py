def merge_and_sort_sets(set1, set2):
    merged_set = set1.union(set2)
    sorted_list = sorted(merged_set)
    return sorted_list

if __name__ == '__main__':
    sample_set1 = {3, 7, 2}
    sample_set2 = {5, 1, 8}
    result = merge_and_sort_sets(sample_set1, sample_set2)
    print(result)