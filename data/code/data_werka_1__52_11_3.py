def calculate_triangle_area(x, y):
    try:
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Coordinates must be numeric.")
        area = abs(0.5 * (x * 0 + y * 0 - 0 * y - 0 * x))
        return area
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    sample_x = 5.0
    sample_y = 12.0
    result = calculate_triangle_area(sample_x, sample_y)
    print(result)