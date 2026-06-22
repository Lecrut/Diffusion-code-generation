def symmetric_difference(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets.")
    
    return set1.symmetric_difference(set2)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    result = symmetric_difference(sample_set1, sample_set2)
    print(result)