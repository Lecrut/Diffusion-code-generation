def compare_length_lists(list1, list2):
    combined_list = list1 + list2
    max_length = max(combined_list)
    min_length = min(combined_list)
    range_difference = max_length - min_length
    return max_length, min_length, range_difference

if __name__ == '__main__':
    lengths1 = [150, 200, 300]
    lengths2 = [100, 400, 250]
    result = compare_length_lists(lengths1, lengths2)
    print(result)