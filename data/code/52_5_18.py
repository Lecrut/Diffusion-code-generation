def calculate_area(dimensions):
    if len(dimensions) == 2:
        base, height = dimensions
        return 0.5 * base * height
    elif len(dimensions) % 2 == 0:
        area = 0
        n = len(dimensions)
        for i in range(n):
            j = (i + 1) % n
            area += dimensions[i] * dimensions[j]
        return abs(area) / 2.0
    else:
        raise ValueError("Unsupported number of dimensions for area calculation.")

if __name__ == '__main__':
    triangle_dimensions1 = [3, 4]
    try:
        area_triangle1 = calculate_area(triangle_dimensions1)
        print(f"Area with dimensions {triangle_dimensions1}: {area_triangle1}")
    except ValueError as e:
        print(f"Error: {e}")

    polygon_dimensions1 = [4, 6, 8, 6]
    try:
        area_polygon1 = calculate_area(polygon_dimensions1)
        print(f"Area with dimensions {polygon_dimensions1}: {area_polygon1}")
    except ValueError as e:
        print(f"Error: {e}")

    invalid_dimensions = [7]
    try:
        area_invalid = calculate_area(invalid_dimensions)
        print(f"Area with dimensions {invalid_dimensions}: {area_invalid}")
    except ValueError as e:
        print(f"Error: {e}")