def validate_dimensions(dimensions):
    if not isinstance(dimensions, tuple) or len(dimensions) != 3:
        raise TypeError("Dimensions must be provided as a tuple of three values.")
    length, width, height = dimensions
    if not all(isinstance(d, (int, float)) for d in [length, width, height]):
        raise TypeError("All dimensions must be numeric.")
    if any(d <= 0 for d in dimensions):
        raise ValueError("All dimensions must be positive.")

def calculate_perimeter(dimensions):
    length, width, height = dimensions
    return 2 * (length + width + height)

if __name__ == '__main__':
    try:
        dimensions = (10, 5, 2)
        validate_dimensions(dimensions)
        result = calculate_perimeter(dimensions)
        print(f"Perimeter for {dimensions}: {result}")
    except (TypeError, ValueError) as e:
        print(e)