def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    dimensions = {'base': 12, 'height': 8}
    area = calculate_triangle_area(dimensions['base'], dimensions['height'])
    print(area)