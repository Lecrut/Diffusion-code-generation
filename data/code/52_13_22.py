def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_values = {
        'base': 12,
        'height': 8
    }
    area = calculate_triangle_area(sample_values['base'], sample_values['height'])
    print(area)