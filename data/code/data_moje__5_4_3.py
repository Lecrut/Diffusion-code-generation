def compare_lengths(list_a, list_b):
    all_values = list_a + list_b
    if not all_values:
        return {"min_length": None, "max_length": None, "range_difference": 0}
    min_val = min(all_values)
    max_val = max(all_values)
    range_diff = max_val - min_val
    return {"min_length": min_val, "max_length": max_val, "range_difference": range_diff}

if __name__ == '__main__':
    sample_list_1 = [10.5, 12.0, 15.3]
    sample_list_2 = [8.2, 14.1, 11.9]
    result = compare_lengths(sample_list_1, sample_list_2)
    print(result)