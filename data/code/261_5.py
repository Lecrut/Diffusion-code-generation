import math
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
    sample1 = [1.0, 2.5, 3.0, 4.5, 5.0]
    sample2 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
    sample3 = [1.0, 2.0, 3.0, 4.0]
    sample4 = [1.0, 2.0]
    sample5 = [1.0, 2.0, 3.0]
    sample6 = [1.0, 1.0, 2.0, 3.0]
    sample7 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    sample8 = []
    print(f"Sample 1: {sample1}, Median: {calculate_median(sample1)}")
    print(f"Sample 2: {sample2}, Median: {calculate_median(sample2)}")
    print(f"Sample 3: {sample3}, Median: {calculate_median(sample3)}")
    print(f"Sample 4: {sample4}, Median: {calculate_median(sample4)}")
    print(f"Sample 5: {sample5}, Median: {calculate_median(sample5)}")
    print(f"Sample 6: {sample6}, Median: {calculate_median(sample6)}")
    print(f"Sample 7: {sample7}, Median: {calculate_median(sample7)}")
    try:
        print(f"Sample 8: {sample8}, Median: {calculate_median(sample8)}")
    except ValueError as e:
        print(f"Sample 8: {sample8}, Error: {e}")