def get_median_from_sorted_list(sorted_list):
    length = len(sorted_list)
    if length == 0:
        return None
    if length % 2 == 1:
        index = length // 2
        return sorted_list[index]
    else:
        index_right = length // 2
        index_left = index_right - 1
        mid_val_1 = sorted_list[index_left]
        mid_val_2 = sorted_list[index_right]
        return (mid_val_1 + mid_val_2) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 2, 4, 6, 8, 10]
    empty_list = []
    single_list = [42]

    print(get_median_from_sorted_list(odd_list))
    print(get_median_from_sorted_list(even_list))
    print(get_median_from_sorted_list(empty_list))
    print(get_median_from_sorted_list(single_list))