def validate_coordinates(p1, p2, p3):
    if not all(isinstance(coord, tuple) and len(coord) == 2 for coord in (p1, p2, p3)):
        raise ValueError("All vertices must be tuples of two numbers.")
    if not all(isinstance(x, (int, float)) and isinstance(y, (int, float)) for x, y in (p1, p2, p3)):
        raise ValueError("Coordinates must be numeric.")

def calculate_triangle_area(p1, p2, p3):
    validate_coordinates(p1, p2, p3)
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)
    return area

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    try:
        area = calculate_triangle_area(*vertices)
        print(f"Area of the triangle: {area:.2f}")
    except ValueError as e:
        print(e)