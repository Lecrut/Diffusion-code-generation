def validate_coordinates(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Coordinates must be integers or floats.")
    return x, y

def calculate_triangle_area(x1, y1):
    x1, y1 = validate_coordinates(x1, y1)
    area = abs(0.5 * (x1 * 0 + y1 * 0 - 0 * y1 - 0 * x1))
    return area

if __name__ == '__main__':
    sample_x = 3
    sample_y = 4
    try:
        area = calculate_triangle_area(sample_x, sample_y)
        print(area)
    except ValueError as e:
        print(e)