def calculate_perimeter(dimensions):
    if len(dimensions) != 2:
        raise ValueError("The dimensions list must contain exactly two elements.")
    
    length, width = dimensions
    
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise TypeError("Both dimensions must be numbers.")
    
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative.")
    
    return 2 * (length + width)

if __name__ == '__main__':
    sample_dimensions = [5, 3]
    try:
        perimeter = calculate_perimeter(sample_dimensions)
        print(perimeter)
    except Exception as e:
        print(e)