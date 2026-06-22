def calculate_median(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2.0
if __name__ == '__main__':
    sample1 = [1.0, 2.5, 3.0, 4.5, 5.0]
    sample2 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
    sample3 = [1.0, 2.0, 3.0, 4.0]
    sample4 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    print(calculate_median(sample1))
    print(calculate_median(sample2))
    print(calculate_median(sample3))
    print(calculate_median(sample4))