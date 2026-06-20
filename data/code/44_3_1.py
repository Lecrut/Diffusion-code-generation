def calculate_perimeter(dimensions):
    if not isinstance(dimensions, (list, tuple)):
        raise TypeError("Dimensions must be a list or tuple")
    if len(dimensions) != 2:
        raise ValueError("Dimensions must contain exactly two elements")
    length, width = dimensions
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Dimensions must be numeric")
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be non-negative")
    return 2 * (length + width)

if __name__ == '__main__':
    sample_dimensions = [5, 10]
    result = calculate_perimeter(sample_dimensions)
    print(result)