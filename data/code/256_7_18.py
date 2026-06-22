def calculate_range(data):
    if not data:
        return None
    
    min_val = float('inf')
    max_val = float('-inf')
    
    for item in data:
        try:
            num = float(item)
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        except ValueError:
            continue
    
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [3.14159, 1.61803, 'a', 2.71828, 0.57721, 4.0, 'b', 1.0]
    range_result = calculate_range(sample_data)
    print(range_result)