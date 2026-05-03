def calculate_triangle_area(base, height):
    try:
        base = float(base)
        height = float(height)
        if base <= 0 or height <= 0:
            return "Error: Base and height must be positive values"
        return base * height
    except ValueError:
        return "Error: Invalid input. Please provide valid numbers"
    except TypeError:
        return "Error: Invalid input types"
if __name__ == '__main__':
    print(calculate_triangle_area(10.0, 5.0))
    print(calculate_triangle_area(7.5, 4.0))
    print(calculate_triangle_area(-2.0, 5.0))
    print(calculate_triangle_area(10.0, 0.0))
    print(calculate_triangle_area("a", 5.0))
    print(calculate_triangle_area(10, "b"))