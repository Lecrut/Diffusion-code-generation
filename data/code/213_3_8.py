def calculate_stats(numbers):
    if not numbers:
        return None, None, None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mean = sum(sorted_numbers) / n
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2.0
    range_val = sorted_numbers[-1] - sorted_numbers[0]
    return mean, median, range_val
if __name__ == '__main__':
    sample_data = [10.5, 20.1, 30.0, 40.9, 50.2]
    mean_val, median_val, range_val = calculate_stats(sample_data)
    print(f"Data: {sample_data}")
    print(f"Mean: {mean_val}")
    print(f"Median: {median_val}")
    print(f"Range: {range_val}")
    sample_data_even = [1, 2, 3, 4]
    mean_val_e, median_val_e, range_val_e = calculate_stats(sample_data_even)
    print(f"\nData: {sample_data_even}")
    print(f"Mean: {mean_val_e}")
    print(f"Median: {median_val_e}")
    print(f"Range: {range_val_e}")
    empty_data = []
    mean_val_e, median_val_e, range_val_e = calculate_stats(empty_data)
    print(f"\nData: {empty_data}")
    print(f"Mean: {mean_val_e}")
    print(f"Median: {median_val_e}")
    print(f"Range: {range_val_e}")