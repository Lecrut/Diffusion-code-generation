def get_median(sorted_list):
    n = len(sorted_list)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

if __name__ == '__main__':
    sorted_data = [1, 3, 5, 7, 9]
    result = get_median(sorted_data)
    print(result)
    sorted_data_even = [2, 4, 6, 8]
    result_even = get_median(sorted_data_even)
    print(result_even)