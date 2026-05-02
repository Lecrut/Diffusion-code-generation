def calculate_triangle_area(base, height):
    try:
        base = float(base)
        height = float(height)
        if base < 0 or height < 0:
            return "Error: Base and height must be non-negative"
        return base * height
    except ValueError:
        return "Error: Invalid input. Please provide valid numbers"
    except TypeError:
        return "Error: Invalid input types"
if __name__ == '__main__':
    print(calculate_triangle_area(4.0, 5.0))
    print(calculate_triangle_area(10.5, 2.0))
    print(calculate_triangle_area(-3.0, 4.0))
    print(calculate_triangle_area("a", 5.0))
    print(calculate_triangle_area(7.0, -2.0))
    print(calculate_triangle_area(10, "b"))