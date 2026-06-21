def validate_coordinates(x1, y1, x2, y2, x3, y3):
    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2, x3, y3]):
        raise ValueError("All coordinates must be numbers.")
    if len({(x1, y1), (x2, y2), (x3, y3)}) < 3:
        raise ValueError("The vertices must not be collinear.")

def triangle_area(x1, y1, x2, y2, x3, y3):
    validate_coordinates(x1, y1, x2, y2, x3, y3)
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

if __name__ == '__main__':
    try:
        area = triangle_area(0, 0, 4, 0, 2, 3)
        print("Area of the triangle:", area)
    except ValueError as e:
        print(e)