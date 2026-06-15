def validate_positive_dimensions(func):
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            raise TypeError("At least three arguments are required for perimeter calculation.")
        dimensions = args[0:3]
        for dim in dimensions:
            if not isinstance(dim, (int, float)) or dim <= 0:
                raise ValueError("All dimensions must be positive numbers.")
        return func(*args, **kwargs)
    return wrapper
@validate_positive_dimensions
def calculate_perimeter(length, width, height):
    return 2 * (length + width + height)
if __name__ == '__main__':
    try:
        result = calculate_perimeter(10, 5, 2)
        print(f"Perimeter: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    try:
        calculate_perimeter(-10, 5, 2)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    try:
        calculate_perimeter(10, 0, 2)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    try:
        calculate_perimeter(10)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")