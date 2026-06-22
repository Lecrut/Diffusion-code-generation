def calculate_median(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid_index = n // 2
    if n % 2 == 1:
        median = sorted_data[mid_index]
    else:
        median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2.0
    return median
if __name__ == '__main__':
    sample1 = [3.5, 1.5, 2.5, 4.5, 5.5]
    sample2 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    print(calculate_median(sample1))
    print(calculate_median(sample2))