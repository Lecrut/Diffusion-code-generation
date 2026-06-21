def find_minimum_magnitude(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    minimum = min(data, key=lambda x: abs(x))
    return minimum

if __name__ == '__main__':
    sample_data = [3+4j, 1-2j, -5+6j, -7-8j]
    print(find_minimum_magnitude(sample_data))