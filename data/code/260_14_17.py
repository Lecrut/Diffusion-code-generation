def is_valid_set(input_set):
    return isinstance(input_set, set) and all(isinstance(item, (int, float)) for item in input_set)

def compare_sets(set1, set2):
    if not is_valid_set(set1) or not is_valid_set(set2):
        raise ValueError("Both inputs must be sets of numbers")
    
    return max(set1, set2, key=len)

if __name__ == '__main__':
    sample_set1 = {3, 5, 2}
    sample_set2 = {4, 6, 1}
    larger_set = compare_sets(sample_set1, sample_set2)
    print(larger_set)