def get_median(data):
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

if __name__ == '__main__':
    sample_values = [7, 1, 3, 9, 5, 2, 8]
    result = get_median(sample_values)
    print(result)