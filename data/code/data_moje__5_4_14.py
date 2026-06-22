def compare_length_lists(list_a, list_b):
    if not list_a and not list_b:
        return {"max_length": 0, "min_length": 0, "range_difference": 0}
    
    all_lengths = list_a + list_b
    
    if not all_lengths:
        return {"max_length": 0, "min_length": 0, "range_difference": 0}
    
    max_val = max(all_lengths)
    min_val = min(all_lengths)
    range_diff = max_val - min_val
    
    return {
        "max_length": max_val,
        "min_length": min_val,
        "range_difference": range_diff
    }

if __name__ == '__main__':
    sample_list_1 = [10.5, 20.3, 5.1, 15.0]
    sample_list_2 = [12.2, 8.7, 25.0, 5.1]
    result = compare_length_lists(sample_list_1, sample_list_2)
    print(result)