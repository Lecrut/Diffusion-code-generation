def calculate_perimeter(dimensions):
    if len(dimensions) != 2:
        raise ValueError("The dimensions list must contain exactly two elements.")
    
    length, width = dimensions
    
    if not all(isinstance(x, (int, float)) and x > 0 for x in dimensions):
        raise ValueError("Both dimensions must be positive numbers.")
    
    return 2 * (length + width)

if __name__ == '__main__':
    sample_dimensions = [5, 3]
    perimeter = calculate_perimeter(sample_dimensions)
    print(perimeter)