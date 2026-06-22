def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    elif n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_data1 = [1, 3, 5, 7, 9]
    sample_data2 = [4, 1, 8, 3, 6]
    sample_data3 = [10, 20, 30, 40]

    print(f"Sample Data 1 Median: {calculate_median(sample_data1)}")
    print(f"Sample Data 2 Median: {calculate_median(sample_data2)}")
    print(f"Sample Data 3 Median: {calculate_median(sample_data3)}")