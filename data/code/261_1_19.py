def calculate_median(data):
    n = len(data)
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

if __name__ == '__main__':
    sample_data1 = [5, 2, 8, 1, 9]
    print(f"Median of {sample_data1}: {calculate_median(sample_data1)}")
    sample_data2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"Median of {sample_data2}: {calculate_median(sample_data2)}")
    sample_data3 = [10, 20, 30, 40]
    print(f"Median of {sample_data3}: {calculate_median(sample_data3)}")
    sample_data4 = [7]
    print(f"Median of {sample_data4}: {calculate_median(sample_data4)}")