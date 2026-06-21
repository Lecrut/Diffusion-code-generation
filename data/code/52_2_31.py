def calculate_triangle_area(base, height):
    if base <= 0:
        raise ValueError("Base must be a positive number.")
    if height <= 0:
        raise ValueError("Height must be a positive number.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        sample_values = {'base': 9, 'height': 4}
        area = calculate_triangle_area(sample_values['base'], sample_values['height'])
        print(area)
    except ValueError as e:
        print(e)