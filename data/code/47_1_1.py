def calculate_triangle_area(base, height):
    try:
        base = float(base)
        height = float(height)
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive values.")
        return 0.5 * base * height
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: Both arguments must be valid numbers. Error: {e}")
if __name__ == '__main__':
    print(calculate_triangle_area(4.0, 5.0))
    print(calculate_triangle_area(10.5, 2.0))
    try:
        calculate_triangle_area(-3.0, 4.0)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_triangle_area("a", 5.0)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_triangle_area(10.0, -2.0)
    except ValueError as e:
        print(f"Error caught: {e}")