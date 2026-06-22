def calculate_median(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    return sorted_data[mid] if n % 2 == 1 else (sorted_data[mid - 1] + sorted_data[mid]) / 2
if __name__ == '__main__':
    print(calculate_median([1, 3, 2]))
    print(calculate_median([5, 1, 4, 2, 8]))
    print(calculate_median([1, 3, 2, 4]))