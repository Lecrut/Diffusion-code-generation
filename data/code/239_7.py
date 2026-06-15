def validate_positive_dimensions(func):
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            raise TypeError("At least three arguments (length, width, height) are required.")
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
        result1 = calculate_perimeter(10, 5, 2)
        print(f"Perimeter for (10, 5, 2): {result1}")
    except (TypeError, ValueError) as e:
        print(f"Error calculating perimeter 1: {e}")
    try:
        result2 = calculate_perimeter(-10, 5, 2)
        print(f"Perimeter for (-10, 5, 2): {result2}")
    except (TypeError, ValueError) as e:
        print(f"Error calculating perimeter 2: {e}")
    try:
        result3 = calculate_perimeter(10, 0, 2)
        print(f"Perimeter for (10, 0, 2): {result3}")
    except (TypeError, ValueError) as e:
        print(f"Error calculating perimeter 3: {e}")
    try:
        result4 = calculate_perimeter(5)
        print(f"Perimeter for (5): {result4}")
    except (TypeError, ValueError) as e:
        print(f"Error calculating perimeter 4: {e}")