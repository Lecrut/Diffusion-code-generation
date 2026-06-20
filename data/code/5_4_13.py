def compare_length_lists(list1, list2):
    combined = list1 + list2
    max_length = max(combined)
    min_length = min(combined)
    range_difference = max_length - min_length
    return max_length, min_length, range_difference

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [5, 15, 25, 35]
    result = compare_length_lists(sample_list1, sample_list2)
    print(result)