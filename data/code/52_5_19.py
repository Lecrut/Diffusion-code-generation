import math

def calculate_area(dimensions):
    if len(dimensions) == 2:
        base, height = dimensions
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive values.")
        return 0.5 * base * height
    elif len(dimensions) % 2 == 0:
        return shoelace_formula(dimensions)
    else:
        raise ValueError("Invalid number of dimensions for area calculation.")

def shoelace_formula(vertices):
    n = len(vertices) // 2
    area = 0.5 * abs(sum(vertices[i] * vertices[(i + 1) % (2 * n)] - vertices[(i + 1) % (2 * n)] * vertices[i] for i in range(0, 2 * n, 2)))
    return area

if __name__ == '__main__':
    triangle_dimensions = [3, 4]
    try:
        triangle_area = calculate_area(triangle_dimensions)
        print(f"Area of triangle with dimensions {triangle_dimensions}: {triangle_area}")
    except ValueError as e:
        print(f"Error: {e}")

    polygon_dimensions = [1, 0, 0, 1, 1, 1]
    try:
        polygon_area = calculate_area(polygon_dimensions)
        print(f"Area of polygon with dimensions {polygon_dimensions}: {polygon_area}")
    except ValueError as e:
        print(f"Error: {e}")