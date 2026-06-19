def is_valid_coordinate(value):
    return isinstance(value, (int, float))

def calculate_triangle_area(x, y):
    if not (is_valid_coordinate(x) and is_valid_coordinate(y)):
        raise ValueError("Coordinates must be numeric.")
    area = abs(0.5 * x * y)
    return area

if __name__ == '__main__':
    sample_x = 7.0
    sample_y = 24.0
    try:
        result = calculate_triangle_area(sample_x, sample_y)
        print(result)
    except ValueError as e:
        print(e)