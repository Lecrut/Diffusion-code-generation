def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    dimensions = {'width': 10, 'height': 5}
    perimeter = calculate_rectangle_perimeter(dimensions['width'], dimensions['height'])
    print(perimeter)