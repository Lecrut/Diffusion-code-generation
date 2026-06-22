def compare_length_ranges(list1, list2):
    max_len = max(max(list1), max(list2))
    min_len = min(min(list1), min(list2))
    range_diff = max_len - min_len
    return max_len, min_len, range_diff

if __name__ == '__main__':
    lengths1 = [10, 20, 30, 40]
    lengths2 = [15, 25, 35, 45]
    max_len, min_len, range_diff = compare_length_ranges(lengths1, lengths2)
    print(max_len, min_len, range_diff)