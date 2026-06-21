def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    triangle_dimensions = {
        'base': 14,
        'height': 9
    }
    area = calculate_triangle_area(triangle_dimensions['base'], triangle_dimensions['height'])
    print(area)