def calculate_numeric_range(data):
    if not data:
        return None
    min_val = float('inf')
    max_val = float('-inf')
    for item in data:
        if isinstance(item, (int, float)):
            if item < min_val:
                min_val = item
            if item > max_val:
                max_val = item
    if min_val == float('inf'):
        return None
    return (min_val, max_val)
if __name__ == '__main__':
    sample_data = [10, 3.5, -5, 22.1, 0, -100]
    result = calculate_numeric_range(sample_data)
    print(result)