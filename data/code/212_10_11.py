def find_min_max(data):
    if not data:
        raise ValueError("List is empty")
    
    minimum = maximum = data[0]
    
    for num in data[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [25, 42, 18, 9, 36]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")