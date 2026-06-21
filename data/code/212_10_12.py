def find_min_max(data):
    if not data:
        raise ValueError("List is empty")
    
    minimum = maximum = data[0]
    
    for value in data[1:]:
        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value
    
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")