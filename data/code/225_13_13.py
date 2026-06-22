def validate_data(data):
    if not isinstance(data, tuple) or len(data) == 0:
        raise ValueError("Input must be a non-empty tuple")

def find_min_max(data):
    validate_data(data)
    return min(data), max(data)

if __name__ == '__main__':
    sample_tuple = (100, 50, 200, 75)
    minimum, maximum = find_min_max(sample_tuple)
    print(f"Sample Tuple: {sample_tuple}")
    print(f"Minimum element: {minimum}")
    print(f"Maximum element: {maximum}")