def compare_length_ranges(list1, list2):
    max_len = max(max(list1), max(list2))
    min_len = min(min(list1), min(list2))
    range_diff = max_len - min_len
    return max_len, min_len, range_diff

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [15, 25, 35, 45]
    
    max_length, min_length, range_difference = compare_length_ranges(sample_list1, sample_list2)
    print(max_length, min_length, range_difference)