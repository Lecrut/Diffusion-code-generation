def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    minimum = float('inf')
    for item in data:
        if isinstance(item, (int, float)) and item < minimum:
            minimum = item
    
    return minimum

if __name__ == '__main__':
    sample_list = [10, 3.14, 5, -2.5, "a", 0]
    try:
        result = find_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")