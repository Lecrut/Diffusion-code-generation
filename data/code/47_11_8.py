def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        return None
    return 0.5 * base * height

if __name__ == '__main__':
    sample_values = {
        'base': 9.0,
        'height': 6.0
    }
    area = calculate_triangle_area(sample_values['base'], sample_values['height'])
    if area is not None:
        print(area)
    else:
        print("Invalid base or height values.")