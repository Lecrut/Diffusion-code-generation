def analyze_lengths(list_a, list_b):
    if not list_a and not list_b:
        return {"max": None, "min": None, "range_diff": None}
    
    combined = list_a + list_b
    if not combined:
        return {"max": None, "min": None, "range_diff": None}
    
    max_val = max(combined)
    min_val = min(combined)
    range_diff = max_val - min_val
    
    return {"max": max_val, "min": min_val, "range_diff": range_diff}

if __name__ == '__main__':
    sample_list_a = [10.5, 20.2, 15.0]
    sample_list_b = [12.1, 30.5, 5.0]
    result = analyze_lengths(sample_list_a, sample_list_b)
    print(result)