def get_median(sorted_list):
    length = len(sorted_list)
    mid_index = length // 2
    if length % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    return sorted_list[mid_index]

if __name__ == '__main__':
    test_sorted_list = [1, 3, 5, 7, 9]
    print(get_median(test_sorted_list))
    test_even_list = [2, 4, 6, 8]
    print(get_median(test_even_list))