def calculate_area(base, height):
    return base * height

if __name__ == '__main__':
    dimensions = {
        'base': 9,
        'height': 4
    }
    area = calculate_area(dimensions['base'], dimensions['height'])
    print(area)