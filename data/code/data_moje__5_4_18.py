def analyze_lengths(list1, list2):
    all_lengths = list1 + list2
    if not all_lengths:
        raise ValueError("At least one list must contain measurements")
    max_length = max(all_lengths)
    min_length = min(all_lengths)
    range_difference = max_length - min_length
    return {"max": max_length, "min": min_length, "range_difference": range_difference}

if __name__ == '__main__':
    sample_list1 = [10.5, 20.0, 15.3]
    sample_list2 = [12.1, 8.7, 25.4]
    result = analyze_lengths(sample_list1, sample_list2)
    print(result)