def compute_area_of_triangle(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    triangle_dimensions = {
        'base': 14.0,
        'height': 6.0
    }
    area = compute_area_of_triangle(triangle_dimensions['base'], triangle_dimensions['height'])
    print(area)