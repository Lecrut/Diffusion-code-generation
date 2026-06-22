def calculate_range(data):
    if not data:
        return None
    filtered_data = [x for x in data if isinstance(x, (int, float))]
    if not filtered_data:
        return None
    min_val = min(filtered_data)
    max_val = max(filtered_data)
    return max_val - min_val

if __name__ == '__main__':
    sample_data = ['a', 3.14159, 1.61803, 'b', 2.71828, 0.57721, 4.0, 1.0]
    range_result = calculate_range(sample_data)
    print(range_result)