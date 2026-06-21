def get_median(sorted_list):
    length = len(sorted_list)
    if length == 0:
        return None
    mid_index = length // 2
    if length % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    else:
        return sorted_list[mid_index]

if __name__ == '__main__':
    test_list_even = [1, 3, 5, 7]
    test_list_odd = [1, 3, 5, 7, 9]
    print(get_median(test_list_even))
    print(get_median(test_list_odd))