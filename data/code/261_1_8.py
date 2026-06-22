def calculate_median(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_data1 = [5, 2, 8, 1, 9]
    print(f"Data: {sample_data1}, Median: {calculate_median(sample_data1)}")
    sample_data2 = [10, 4, 7, 2, 9, 1]
    print(f"Data: {sample_data2}, Median: {calculate_median(sample_data2)}")
    sample_data3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"Data: {sample_data3}, Median: {calculate_median(sample_data3)}")
    sample_data4 = [1, 2, 3, 4, 5]
    print(f"Data: {sample_data4}, Median: {calculate_median(sample_data4)}")