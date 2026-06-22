def calculate_median(values):
    values.sort()
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2.0
    else:
        return float(values[mid])

if __name__ == '__main__':
    sample_values = [7.5, 3.2, 9.8, 4.6, 5.4]
    median_value = calculate_median(sample_values)
    print(median_value)