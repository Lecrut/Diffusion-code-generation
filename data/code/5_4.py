def compare_lengths(list_a, list_b):
    if not list_a and not list_b:
        return {"max_length": None, "min_length": None, "range_difference": 0}
    
    combined_list = list_a + list_b
    
    if not combined_list:
        return {"max_length": None, "min_length": None, "range_difference": 0}
    
    max_len = max(combined_list)
    min_len = min(combined_list)
    range_diff = max_len - min_len
    
    return {
        "max_length": max_len,
        "min_length": min_len,
        "range_difference": range_diff
    }

if __name__ == '__main__':
    sample_list_a = [10.5, 20.3, 5.0, 15.7]
    sample_list_b = [12.1, 18.9, 5.0, 25.4]
    
    result = compare_lengths(sample_list_a, sample_list_b)
    print(result)