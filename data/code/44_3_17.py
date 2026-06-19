def calculate_perimeter(dimensions):
    REQUIRED_DIMENSIONS = 2

    if len(dimensions) != REQUIRED_DIMENSIONS:
        raise ValueError("The dimensions list must contain exactly two elements.")
    
    length, width = dimensions
    
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise TypeError("Both dimensions must be numbers.")
    
    if length <= 0 or width <= 0:
        raise ValueError("Both dimensions must be positive numbers.")
    
    return 2 * (length + width)

if __name__ == '__main__':
    sample_dimensions = [10, 4]
    try:
        result = calculate_perimeter(sample_dimensions)
        print(result)
    except Exception as e:
        print(e)