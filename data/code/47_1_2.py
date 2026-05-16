def calculate_triangle_area(base, height):
    try:
        base = float(base)
        height = float(height)
        if base < 0 or height < 0:
            raise ValueError("Base and height must be non-negative.")
        return 0.5 * base * height
    except (TypeError, ValueError):
        return "Error: Invalid input. Please provide two valid numbers."
if __name__ == '__main__':
    print(calculate_triangle_area(10.0, 5.0))
    print(calculate_triangle_area(7.5, 4.0))
    print(calculate_triangle_area(-2.0, 5.0))
    print(calculate_triangle_area("a", 5.0))
    print(calculate_triangle_area(12, "b"))
    print(calculate_triangle_area(0.0, 100.0))