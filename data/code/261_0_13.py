import math

def calculate_median(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_data[mid_index]
    else:
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2.0
if __name__ == '__main__':
    sample_list_odd = [5, 2, 8, 1, 9]
    sample_list_even = [10, 4, 7, 2]
    median_odd = calculate_median(sample_list_odd)
    median_even = calculate_median(sample_list_even)
    print(median_odd)
    print(median_even)