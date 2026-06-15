def validate_perimeter(func):
    def wrapper(*args, **kwargs):
        if len(args) < 2:
            raise ValueError("Perimeter calculation requires at least two dimensions.")
        dimensions = [d for d in args if isinstance(d, (int, float))]
        if len(dimensions) != len(args):
            raise TypeError("All arguments must be numeric.")
        for dim in dimensions:
            if dim <= 0:
                raise ValueError("Dimensions must be positive numbers.")
        return func(*args, **kwargs)
    return wrapper
@validate_perimeter
def calculate_perimeter(length, width):
    return 2 * (length + width)
if __name__ == '__main__':
    try:
        result1 = calculate_perimeter(10, 5)
        print(f"Perimeter of 10 and 5: {result1}")
        result2 = calculate_perimeter(7.5, 3)
        print(f"Perimeter of 7.5 and 3: {result2}")
        try:
            calculate_perimeter(-10, 5)
        except ValueError as e:
            print(f"Error caught for negative input: {e}")
        try:
            calculate_perimeter(10, 0)
        except ValueError as e:
            print(f"Error caught for zero input: {e}")
        try:
            calculate_perimeter(10)
        except ValueError as e:
            print(f"Error caught for insufficient arguments: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")