def find_min_value(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_val = float('inf')
    for number in data:
        if number < min_val:
            min_val = number
    return min_val

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, -2.1, 0.0]
    result = find_min_value(sample_values)
    print(result)