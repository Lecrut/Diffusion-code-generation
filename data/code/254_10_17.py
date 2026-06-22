def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_val = data[0]
    for item in data[1:]:
        if item < min_val:
            min_val = item
    return min_val

if __name__ == '__main__':
    sample_list = [3, 2, 4, 5, 9, 7, 6]
    try:
        result = find_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)