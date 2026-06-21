def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_params = {
        'base': 14,
        'height': 7
    }
    try:
        area = calculate_triangle_area(sample_params['base'], sample_params['height'])
        print(area)
    except ValueError as e:
        print(e)