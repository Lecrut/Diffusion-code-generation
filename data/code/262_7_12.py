def is_valid_data(data):
    if not isinstance(data, list) or not data:
        return False
    for item in data:
        if not (isinstance(item, int) or isinstance(item, list)):
            return False
    return True

def find_min_max_recursively(data):
    minimum = float('inf')
    maximum = float('-inf')
    
    for item in data:
        if isinstance(item, list):
            sub_min, sub_max = find_min_max_recursively(item)
            if sub_min < minimum:
                minimum = sub_min
            if sub_max > maximum:
                maximum = sub_max
        else:
            if item < minimum:
                minimum = item
            if item > maximum:
                maximum = item
                
    return minimum, maximum

def find_min_max(data):
    if not is_valid_data(data):
        raise ValueError("Invalid data input")
    
    return find_min_max_recursively(data)

if __name__ == '__main__':
    sample_data = [[3, 1], [4, 1, 5], [9, 2], [6]]
    try:
        min_val, max_val = find_min_max(sample_data)
        print(f"Minimum: {min_val}, Maximum: {max_val}")
    except ValueError as e:
        print(e)