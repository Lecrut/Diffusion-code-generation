def compare_length_measurements(list_a, list_b):
    all_values = list_a + list_b
    if not all_values:
        return {
            "max_length": None,
            "min_length": None,
            "range_difference": None
        }
    max_length = max(all_values)
    min_length = min(all_values)
    range_difference = max_length - min_length
    return {
        "max_length": max_length,
        "min_length": min_length,
        "range_difference": range_difference
    }

if __name__ == '__main__':
    sample_list_a = [10.5, 20.0, 15.3]
    sample_list_b = [18.7, 5.2, 22.1]
    result = compare_length_measurements(sample_list_a, sample_list_b)
    print(result)