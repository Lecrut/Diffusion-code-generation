def compare_length_ranges(list1, list2):
    max_len1 = max(list1)
    min_len1 = min(list1)
    max_len2 = max(list2)
    min_len2 = min(list2)
    
    overall_max = max(max_len1, max_len2)
    overall_min = min(min_len1, min_len2)
    
    range_difference = overall_max - overall_min
    
    return {
        'max_length': overall_max,
        'min_length': overall_min,
        'range_difference': range_difference
    }

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [15, 25, 35, 45]
    
    result = compare_length_ranges(sample_list1, sample_list2)
    print(result)