def compare_length_lists(list1, list2):
    max_length = max(max(list1), max(list2))
    min_length = min(min(list1), min(list2))
    range_difference = max_length - min_length
    return max_length, min_length, range_difference

if __name__ == '__main__':
    lengths1 = [150, 160, 170, 180]
    lengths2 = [140, 190, 155, 165]
    max_length, min_length, range_difference = compare_length_lists(lengths1, lengths2)
    print(f"Max Length: {max_length}, Min Length: {min_length}, Range Difference: {range_difference}")