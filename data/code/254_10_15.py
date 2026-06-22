def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_val = data[0]
    for value in data[1:]:
        if value < min_val:
            min_val = value
    return min_val

if __name__ == '__main__':
    sample_list = [7, 3, 5, 9, 2, 8, 4, 6, 0, 1]
    try:
        result = find_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")