def median_of_sorted_list(sorted_list):
    length = len(sorted_list)
    if length == 0:
        return None
    mid_index = (length - 1) // 2
    if length % 2 == 1:
        return sorted_list[mid_index]
    else:
        right_index = mid_index + 1
        return (sorted_list[mid_index] + sorted_list[right_index]) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 3, 5, 7]
    print(median_of_sorted_list(odd_list))
    print(median_of_sorted_list(even_list))
    print(median_of_sorted_list([42]))
    print(median_of_sorted_list([]))