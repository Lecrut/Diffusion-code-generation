def compare_length_lists(list1, list2):
    all_lengths = list1 + list2
    max_length = max(all_lengths)
    min_length = min(all_lengths)
    range_difference = max_length - min_length
    return max_length, min_length, range_difference

if __name__ == '__main__':
    sample_list1 = [10, 15, 20, 25, 30]
    sample_list2 = [5, 12, 18, 22, 28]
    result = compare_length_lists(sample_list1, sample_list2)
    print(result)