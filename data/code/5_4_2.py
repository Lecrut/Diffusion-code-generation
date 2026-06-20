def compare_lengths(list1, list2):
    if not list1 or not list2:
        raise ValueError("Both lists must be non-empty")
    
    all_lengths = list1 + list2
    max_len = max(all_lengths)
    min_len = min(all_lengths)
    range_diff = max_len - min_len
    
    return {
        'max_length': max_len,
        'min_length': min_len,
        'range_difference': range_diff
    }

if __name__ == '__main__':
    measurements1 = [10.5, 20.3, 15.7, 25.1]
    measurements2 = [12.0, 18.5, 22.4, 19.8]
    
    result = compare_lengths(measurements1, measurements2)
    print(result)