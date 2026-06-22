def find_median(values):
    n = len(values)
    sorted_values = sorted(values)
    mid = n // 2
    
    if n % 2 == 1:
        return float(sorted_values[mid])
    else:
        left = sorted_values[mid - 1]
        right = sorted_values[mid]
        return (left + right) / 2.0

if __name__ == '__main__':
    sample_values = [4.5, 2.3, 6.7, 1.9, 3.2, 5.8]
    median_value = find_median(sample_values)
    print(median_value)