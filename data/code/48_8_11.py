def calculate_area(base, height):
    return base * height

if __name__ == '__main__':
    dimensions = {'base': 6.0, 'height': 4.5}
    area_result = calculate_area(dimensions['base'], dimensions['height'])
    print(area_result)