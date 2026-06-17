def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2.0
if __name__ == '__main__':
    sample1 = [1.0, 5.5, 2.0, 8.1, 3.3]
    sample2 = [1.0, 2.0, 3.0, 4.0]
    sample3 = [1.5, 2.5]
    sample4 = [1.0, 2.0, 3.0, 4.0, 5.0]
    sample5 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    sample6 = [1.1, 2.2, 3.3, 4.4]
    sample7 = [1.0, 1.0, 5.0, 5.0]
    print(f"Sample 1: {sample1}, Median: {calculate_median(sample1)}")
    print(f"Sample 2: {sample2}, Median: {calculate_median(sample2)}")
    print(f"Sample 3: {sample3}, Median: {calculate_median(sample3)}")
    print(f"Sample 4: {sample4}, Median: {calculate_median(sample4)}")
    print(f"Sample 5: {sample5}, Median: {calculate_median(sample5)}")
    print(f"Sample 6: {sample6}, Median: {calculate_median(sample6)}")
    print(f"Sample 7: {sample7}, Median: {calculate_median(sample7)}")