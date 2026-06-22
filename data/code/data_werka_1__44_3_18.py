def calculate_perimeter(dimensions):
    if len(dimensions) != 2:
        raise ValueError("The dimensions list must contain exactly two elements.")
    
    length, width = dimensions
    
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise TypeError("Both length and width must be numbers.")
    
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    sample_dimensions = [5, 3]
    try:
        result = calculate_perimeter(sample_dimensions)
        print(result)
    except Exception as e:
        print(f"Error: {e}")