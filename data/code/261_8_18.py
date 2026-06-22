def calculate_median(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a list of numbers")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

if __name__ == '__main__':
    samples = [
        [1, 5, 2, 8],
        [10, 20, 30, 40, 50],
        [7, 1, 4, 9, 2]
    ]
    
    for sample in samples:
        print(calculate_median(sample))