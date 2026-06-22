def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_val = max_val = data[0]
    for element in data[1:]:
        if element < min_val:
            min_val = element
        elif element > max_val:
            max_val = element
    return (min_val, max_val)

if __name__ == '__main__':
    sample_values = [7, 3, 9, 2, 5, 1, 8, 6]
    result = find_min_max(sample_values)
    print(result)