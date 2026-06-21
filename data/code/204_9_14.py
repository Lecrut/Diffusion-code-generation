def find_median(values):
    values.sort()
    n = len(values)
    if n % 2 == 1:
        return values[n // 2]
    else:
        return (values[n // 2 - 1] + values[n // 2]) / 2

if __name__ == '__main__':
    sample_values_odd = [3, 1, 4, 1, 5, 9, 2]
    median_odd = find_median(sample_values_odd)
    print(f"Median of {sample_values_odd}: {median_odd}")
    
    sample_values_even = [3, 1, 4, 1, 5, 9, 2, 6]
    median_even = find_median(sample_values_even)
    print(f"Median of {sample_values_even}: {median_even}")