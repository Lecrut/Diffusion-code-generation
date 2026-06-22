def is_subset(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets")
    
    return set1.issubset(set2)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3}
    sample_set2 = {1, 2, 3, 4, 5}
    result = is_subset(sample_set1, sample_set2)
    print(result)