def validate_data(data):
    if not data:
        raise ValueError("Data must contain at least one element")
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements must be numbers")

def find_min_max(data):
    validate_data(data)
    return min(data), max(data)

if __name__ == '__main__':
    sample_tuple = (100, 50, 200, 75)
    minimum, maximum = find_min_max(sample_tuple)
    print(f"Sample Tuple: {sample_tuple}")
    print(f"Minimum element: {minimum}")
    print(f"Maximum element: {maximum}")