def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2.0
    return median

if __name__ == '__main__':
    sample_values = {
        'odd': [3.5, 1.0, 4.5, 2.0, 1.5],
        'even': [10.0, 20.0, 30.0, 40.0],
        'single': [99.9],
        'empty': []
    }
    
    for key, value in sample_values.items():
        result = find_median(value)
        print(f"Median of {key}: {result}")