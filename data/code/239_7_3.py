def validate_positive_dimensions(func):
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            raise TypeError("Function requires at least three arguments (length, width, height).")
        length, width, height = args[0], args[1], args[2]
        if not all(isinstance(d, (int, float)) and d > 0 for d in [length, width, height]):
            raise ValueError("All dimensions must be positive numbers.")
        return func(*args, **kwargs)
    return wrapper
@validate_positive_dimensions
def calculate_perimeter(length, width, height):
    perimeter = 2 * (length + width + height)
    return perimeter
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
        calculate_perimeter(5)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")