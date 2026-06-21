def find_min_max(data):
    if not data:
        return None, None
    
    minimum = data[0]
    maximum = data[0]
    
    for value in data:
        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value
    
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 100.0, -50.2]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")