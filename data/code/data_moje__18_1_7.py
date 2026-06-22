def get_median(sorted_list):
    length = len(sorted_list)
    if length == 0:
        raise ValueError("List cannot be empty")
    if length % 2 == 1:
        mid_index = length // 2
        return sorted_list[mid_index]
    else:
        mid_index_upper = length // 2
        mid_index_lower = mid_index_upper - 1
        return (sorted_list[mid_index_lower] + sorted_list[mid_index_upper]) / 2

if __name__ == '__main__':
    test_data_odd = [1, 3, 5, 7, 9]
    test_data_even = [2, 4, 6, 8]
    result_odd = get_median(test_data_odd)
    result_even = get_median(test_data_even)
    print(result_odd)
    print(result_even)