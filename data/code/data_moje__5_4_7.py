def compare_length_lists(list1, list2):
    all_lengths = list1 + list2
    if not all_lengths:
        return None, None, 0
    max_len = max(all_lengths)
    min_len = min(all_lengths)
    range_diff = max_len - min_len
    return max_len, min_len, range_diff

if __name__ == '__main__':
    list_a = [10.5, 20.3, 5.7, 15.0]
    list_b = [12.1, 18.9, 7.2, 14.5]
    result = compare_length_lists(list_a, list_b)
    print(result)