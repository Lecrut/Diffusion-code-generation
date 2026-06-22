def compare_length_lists(list1, list2):
    combined = list1 + list2
    max_length = max(combined)
    min_length = min(combined)
    range_difference = max_length - min_length
    return max_length, min_length, range_difference

if __name__ == '__main__':
    lengths_a = [12.5, 7.3, 9.8, 15.1, 6.2]
    lengths_b = [10.0, 8.7, 14.3, 5.5, 11.9]
    result = compare_length_lists(lengths_a, lengths_b)
    print(result)