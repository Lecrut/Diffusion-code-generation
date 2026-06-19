def compare_length_ranges(list1, list2):
    max_length = max(max(list1), max(list2))
    min_length = min(min(list1), min(list2))
    range_difference = max_length - min_length
    return max_length, min_length, range_difference

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [5, 15, 25, 35]
    max_length, min_length, range_difference = compare_length_ranges(sample_list1, sample_list2)
    print(max_length, min_length, range_difference)