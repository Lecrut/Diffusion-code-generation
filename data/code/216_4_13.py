def calculate_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 != 0:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    median_value = calculate_median(sample_list)
    print(median_value)