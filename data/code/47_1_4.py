def calculate_triangle_area(base, height):
    try:
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Inputs must be numbers.")
        area = base * height
        if area < 0:
            raise ValueError("Area cannot be negative.")
        return area
    except TypeError:
        return "Error: Both inputs must be numbers."
    except ValueError:
        return "Error: Base and height must be non-negative."
    except Exception:
        return "Error: An unexpected error occurred."
if __name__ == '__main__':
    print(calculate_triangle_area(4.0, 5.0))
    print(calculate_triangle_area(10, 2.5))
    print(calculate_triangle_area(-3.0, 4.0))
    print(calculate_triangle_area("a", 5.0))
    print(calculate_triangle_area(7.0, -2.0))
    print(calculate_triangle_area(10, "b"))