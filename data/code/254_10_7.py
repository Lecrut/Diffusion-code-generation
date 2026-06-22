def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_value = data[0]
    for value in data[1:]:
        if value < min_value:
            min_value = value
    return min_value

if __name__ == '__main__':
    sample_list = [34, 22, 56, 78, 1, 90, 0, 12]
    try:
        result = find_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)