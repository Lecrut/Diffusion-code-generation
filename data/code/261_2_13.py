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
    sample_data1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    median1 = calculate_median(sample_data1)
    print(f"Data: {sample_data1}, Median: {median1}")