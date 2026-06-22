def find_median(values):
    values_sorted = sorted(values)
    n = len(values_sorted)
    mid = n // 2
    if n % 2 == 0:
        return (values_sorted[mid - 1] + values_sorted[mid]) / 2.0
    else:
        return float(values_sorted[mid])

if __name__ == '__main__':
    sample_values = [7.5, 3.2, 6.8, 4.9, 2.1, 5.4]
    median_value = find_median(sample_values)
    print(median_value)