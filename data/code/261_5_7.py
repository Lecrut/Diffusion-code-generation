def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2.0
    return median
if __name__ == '__main__':
    sample1 = [1.0, 5.5, 2.0, 8.1, 3.3]
    sample2 = [1.0, 2.0, 3.0, 4.0]
    sample3 = [1.5, 2.5, 3.5, 4.5]
    sample4 = [1.0, 2.0]
    sample5 = [1.0, 2.0, 3.0]
    sample6 = [1.0, 2.0, 3.0, 4.0, 5.0]
    sample7 = [1.0, 1.0, 2.0, 2.0, 3.0, 3.0]
    print(f"Sample 1: {calculate_median(sample1)}")
    print(f"Sample 2: {calculate_median(sample2)}")
    print(f"Sample 3: {calculate_median(sample3)}")
    print(f"Sample 4: {calculate_median(sample4)}")
    print(f"Sample 5: {calculate_median(sample5)}")
    print(f"Sample 6: {calculate_median(sample6)}")
    print(f"Sample 7: {calculate_median(sample7)}")