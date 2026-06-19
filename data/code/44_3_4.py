def validate_dimensions(dimensions):
    if len(dimensions) != 2:
        raise ValueError("The dimensions list must contain exactly two elements.")
    length, width = dimensions
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise TypeError("Both dimensions must be numbers.")
    if length <= 0 or width <= 0:
        raise ValueError("Both dimensions must be positive numbers.")

def calculate_perimeter(dimensions):
    validate_dimensions(dimensions)
    length, width = dimensions
    return 2 * (length + width)

if __name__ == '__main__':
    sample_dimensions = [10, 4]
    try:
        perimeter = calculate_perimeter(sample_dimensions)
        print(perimeter)
    except Exception as e:
        print(e)