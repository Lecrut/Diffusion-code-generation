def calculate_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    rectangle_dimensions = {'width': 4, 'height': 6}
    perimeter = calculate_perimeter(rectangle_dimensions['width'], rectangle_dimensions['height'])
    print(perimeter)