def get_median_from_sorted_list(sorted_list):
    length = len(sorted_list)
    if length == 0:
        return None
    mid_index = length // 2
    if length % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    return sorted_list[mid_index]

if __name__ == '__main__':
    test_list_1 = [1, 3, 4, 5, 9]
    test_list_2 = [2, 4, 6, 8]
    test_list_3 = []
    
    result_1 = get_median_from_sorted_list(test_list_1)
    result_2 = get_median_from_sorted_list(test_list_2)
    result_3 = get_median_from_sorted_list(test_list_3)
    
    print(result_1)
    print(result_2)
    print(result_3)