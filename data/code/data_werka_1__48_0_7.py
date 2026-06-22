def calculate_area(base, height):
    return base * height

if __name__ == '__main__':
    rectangle_dimensions = {
        'base': 6,
        'height': 8
    }
    area = calculate_area(rectangle_dimensions['base'], rectangle_dimensions['height'])
    print(area)