def compare_measurements(list_a, list_b):
    all_values = []
    if list_a:
        all_values.extend(list_a)
    if list_b:
        all_values.extend(list_b)
    if not all_values:
        raise ValueError("Lists are empty")
    min_len = min(all_values)
    max_len = max(all_values)
    range_diff = max_len - min_len
    return {"max": max_len, "min": min_len, "range_diff": range_diff}

if __name__ == '__main__':
    sample_a = [10.5, 20.0, 15.5]
    sample_b = [5.0, 25.0, 12.0]
    result = compare_measurements(sample_a, sample_b)
    print(result)