import math
def find_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    sample_data = [1, 3, 5, 7, 9]
    median_value = find_median(sample_data)
    print(median_value)
    sample_data_even = [1, 2, 3, 4]
    median_value_even = find_median(sample_data_even)
    print(median_value_even)
    sample_data_odd = [10, 20, 5, 15, 25]
    median_value_odd = find_median(sample_data_odd)
    print(median_value_odd)
    sample_data_empty = []
    median_value_empty = find_median(sample_data_empty)
    print(median_value_empty)