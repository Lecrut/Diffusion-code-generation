def get_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

if __name__ == '__main__':
    sample_data = [7, 3, 1, 4, 6, 2, 5]
    result = get_median(sample_data)
    print(result)