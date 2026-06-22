def calculate_triangle_area(x, y):
    return abs(0.5 * (x * 0 + y * 0 - 0 * y - 0 * x))

if __name__ == '__main__':
    sample_coordinates = {'x': 6, 'y': 8}
    area = calculate_triangle_area(sample_coordinates['x'], sample_coordinates['y'])
    print(area)