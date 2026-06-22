def get_median(sorted_list):
    length = len(sorted_list)
    if length == 0:
        return None
    if length % 2 == 1:
        middle_index = length // 2
        return sorted_list[middle_index]
    else:
        right_index = length // 2
        left_index = right_index - 1
        return (sorted_list[left_index] + sorted_list[right_index]) / 2.0

if __name__ == '__main__':
    test_list_odd = [1, 3, 5, 7, 9]
    test_list_even = [2, 4, 6, 8, 10, 12]
    result_odd = get_median(test_list_odd)
    result_even = get_median(test_list_even)
    print(result_odd)
    print(result_even)