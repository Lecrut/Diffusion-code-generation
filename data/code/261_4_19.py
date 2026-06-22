def find_median(values):
    if not values:
        return None
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 1:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2.0

if __name__ == '__main__':
    sample_values = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    median_value = find_median(sample_values)
    print(median_value)