def compare_lengths(list1, list2):
    combined = list1 + list2
    if not combined:
        return {"min": None, "max": None, "range": None}
    
    min_val = min(combined)
    max_val = max(combined)
    range_val = max_val - min_val
    
    return {"min": min_val, "max": max_val, "range": range_val}

if __name__ == '__main__':
    sample_list1 = [10.5, 20.3, 15.0]
    sample_list2 = [12.0, 18.5, 25.0]
    result = compare_lengths(sample_list1, sample_list2)
    print(result)