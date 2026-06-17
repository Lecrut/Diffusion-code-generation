def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2
    return median
if __name__ == '__main__':
    samples = [1, 5, 2, 8, 3]
    for sample in samples:
        median_value = calculate_median([sample])
        print(f"The sample is: {sample}, the median is: {median_value}")