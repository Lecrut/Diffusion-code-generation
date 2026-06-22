def compare_sets(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets.")
    
    return max(set1, set2, key=len)

if __name__ == '__main__':
    sample_set1 = {3, 5, 2}
    sample_set2 = {4, 6, 1}
    larger_set = compare_sets(sample_set1, sample_set2)
    print(larger_set)