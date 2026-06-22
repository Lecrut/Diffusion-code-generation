def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

if __name__ == '__main__':
    sample_data_odd = [3, 1, 2, 4, 5]
    median_value_odd = find_median(sample_data_odd)
    print(median_value_odd)

    sample_data_even = [-10, 4, 6, 1000, 10, 20]
    median_value_even = find_median(sample_data_even)
    print(median_value_even)

    empty_list = []
    median_value_empty = find_median(empty_list)
    print(median_value_empty)