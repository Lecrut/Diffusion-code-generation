def find_min_max(data):
    if not data:
        raise ValueError("Empty list provided")
    
    minimum = maximum = data[0]
    
    for num in data[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [12, 34, 56, 78, 90, 23, 45]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")