def calculate_perimeter(dimensions):
    if len(dimensions) != 2:
        raise ValueError("Exactly two dimensions are required.")
    
    length, width = dimensions
    
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    sample_dimensions = [5, 10]
    try:
        result = calculate_perimeter(sample_dimensions)
        print(result)
    except Exception as e:
        print(e)