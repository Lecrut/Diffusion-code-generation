def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    minimum = data[0]
    maximum = data[0]
    
    for number in data:
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
    
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")