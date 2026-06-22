def find_range(data):
    if not data:
        return None
    min_val = float('inf')
    max_val = float('-inf')
    for x in data:
        try:
            val = float(x)
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
        except ValueError:
            continue
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [3.14159, 1.61803, 'text', 2.71828, 0.57721, 4.0, None]
    range_result = find_range(sample_data)
    print(range_result)