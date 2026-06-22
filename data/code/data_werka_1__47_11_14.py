def compute_triangle_area(dimensions):
    base = dimensions['base']
    height = dimensions['height']
    return 0.5 * base * height

if __name__ == '__main__':
    triangle_dimensions = {
        'base': 9.0,
        'height': 4.0
    }
    area = compute_triangle_area(triangle_dimensions)
    print(area)