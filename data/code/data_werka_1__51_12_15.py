def calculate_rectangle_perimeter(dimensions):
    return 2 * (dimensions['width'] + dimensions['height'])

if __name__ == '__main__':
    rectangle_dimensions = {'width': 8, 'height': 6}
    perimeter = calculate_rectangle_perimeter(rectangle_dimensions)
    print(perimeter)