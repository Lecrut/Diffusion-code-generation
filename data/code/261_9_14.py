def find_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

if __name__ == '__main__':
    sample_data = [1, 3, 5, 7, 9]
    median_value = find_median(sample_data)
    print(median_value)
    sample_data_even = [1, 2, 3, 4]
    median_value_even = find_median(sample_data_even)
    print(median_value_even)