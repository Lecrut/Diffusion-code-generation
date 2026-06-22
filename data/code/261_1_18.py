def calculate_median(data):
    n = len(data)
    sorted_data = sorted(data)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_data[mid_index]
    else:
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2

if __name__ == '__main__':
    sample_data1 = [7, 3, 9, 4, 2, 8]
    print(f"Data: {sample_data1}, Median: {calculate_median(sample_data1)}")
    
    sample_data2 = [15, 6, 22, 18, 13, 10]
    print(f"Data: {sample_data2}, Median: {calculate_median(sample_data2)}")