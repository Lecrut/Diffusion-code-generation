def merge_and_sort_sets(set1, set2):
    combined_set = set1.union(set2)
    sorted_list = sorted(combined_set)
    return sorted_list

if __name__ == '__main__':
    sample_set1 = {3, 1, 4}
    sample_set2 = {2, 5, 6}
    result = merge_and_sort_sets(sample_set1, sample_set2)
    print(result)