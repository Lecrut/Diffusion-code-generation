def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

if __name__ == '__main__':
    sample_data1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sample_data2 = [10, 20, 30, 40, 50]
    sample_data3 = []

    print(f"Median of {sample_data1}: {calculate_median(sample_data1)}")
    print(f"Median of {sample_data2}: {calculate_median(sample_data2)}")
    print(f"Median of {sample_data3}: {calculate_median(sample_data3)}")