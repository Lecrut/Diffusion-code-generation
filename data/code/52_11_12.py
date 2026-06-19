def calculate_triangle_area(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "Coordinates must be numeric."
    return abs(0.5 * x * y)

if __name__ == '__main__':
    sample_x = 6
    sample_y = 8
    area = calculate_triangle_area(sample_x, sample_y)
    print(area)