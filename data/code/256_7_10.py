def find_range(data):
    if not data:
        return None
    
    try:
        min_val = max_val = float(data[0])
        
        for x in data[1:]:
            num = float(x)
            if num < min_val:
                min_val = num
            elif num > max_val:
                max_val = num
        
        return max_val - min_val
    except ValueError:
        return None

if __name__ == '__main__':
    sample_data = [3.14159, 1.61803, 'a', 2.71828, 0.57721, 4.0, 1.0]
    range_result = find_range(sample_data)
    print(range_result)