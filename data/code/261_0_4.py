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
    sample_list_odd = [5, 2, 8, 1, 9]
    sample_list_even = [10, 4, 7, 2]
    median_odd = calculate_median(sample_list_odd)
    print(f"Median of {sample_list_odd}: {median_odd}")
    median_even = calculate_median(sample_list_even)
    print(f"Median of {sample_list_even}: {median_even}")