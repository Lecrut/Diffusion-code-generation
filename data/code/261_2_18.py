def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_data[mid_index]
    else:
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2.0

if __name__ == '__main__':
    sample_data1 = [1, 3, 5, 7, 9]
    sample_data2 = [4, 1, 8, 3, 6]
    sample_data3 = [10, 20, 30, 40]

    print(f"Median of {sample_data1} is: {calculate_median(sample_data1)}")
    print(f"Median of {sample_data2} is: {calculate_median(sample_data2)}")
    print(f"Median of {sample_data3} is: {calculate_median(sample_data3)}")