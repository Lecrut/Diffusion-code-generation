def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    triangle_dimensions = {
        'base': 9.0,
        'height': 4.0
    }
    area = calculate_triangle_area(triangle_dimensions['base'], triangle_dimensions['height'])
    print(area)