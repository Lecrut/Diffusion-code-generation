MAX_LENGTH = 1000
MIN_LENGTH = -1000

def find_min_max_by_length(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    
    minimum = max(MIN_LENGTH, len(data[0]))
    maximum = min(MAX_LENGTH, len(data[0]))
    
    for x in data:
        length = len(x)
        if length < minimum:
            minimum = length
        if length > maximum:
            maximum = length
    
    return minimum, maximum

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    min_val, max_val = find_min_max_by_length(sample_data)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")