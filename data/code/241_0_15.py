def calculate_area(width, height):
    return width * height

if __name__ == '__main__':
    dimensions = {'width': 5, 'height': 3}
    area = calculate_area(dimensions['width'], dimensions['height'])
    print(area)