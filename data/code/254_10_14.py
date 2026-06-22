def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    MIN_INDEX = 0
    minimum = data[MIN_INDEX]
    
    for i in range(1, len(data)):
        if data[i] < minimum:
            minimum = data[i]
    
    return minimum

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    try:
        result = find_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")