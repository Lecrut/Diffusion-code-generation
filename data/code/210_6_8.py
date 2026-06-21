def compute_range(data):
    min_val = next((x for x in data if not isinstance(x, (str, bytes))), None)
    max_val = next((x for x in data if not isinstance(x, (str, bytes))), None)
    
    for value in data:
        if not isinstance(value, (str, bytes)):
            if min_val is None or value < min_val:
                min_val = value
            if max_val is None or value > max_val:
                max_val = value
    
    return min_val, max_val

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(compute_range(sample_data))