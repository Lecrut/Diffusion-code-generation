def compare_length_measurements(list1, list2):
    if not list1 and not list2:
        return {"max_length": None, "min_length": None, "range_difference": None}
    
    all_lengths = list1 + list2
    
    max_length = max(all_lengths)
    min_length = min(all_lengths)
    range_difference = max_length - min_length
    
    return {
        "max_length": max_length,
        "min_length": min_length,
        "range_difference": range_difference
    }

if __name__ == '__main__':
    measurements_a = [10.5, 20.3, 5.7, 15.2]
    measurements_b = [18.1, 30.0, 2.5, 12.8]
    
    result = compare_length_measurements(measurements_a, measurements_b)
    print(result)