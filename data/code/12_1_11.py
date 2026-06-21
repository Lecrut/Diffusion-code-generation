def get_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

if __name__ == '__main__':
    sample_data = [7, 1, 3, 4, 6, 5, 2]
    result = get_median(sample_data)
    print(result)