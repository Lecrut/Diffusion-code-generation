def merge_and_sort_sets(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets")
    
    unique_elements = set1.union(set2)
    return sorted(unique_elements)

if __name__ == '__main__':
    sample_set1 = {3, 1, 4}
    sample_set2 = {2, 5, 6}
    print(merge_and_sort_sets(sample_set1, sample_set2))