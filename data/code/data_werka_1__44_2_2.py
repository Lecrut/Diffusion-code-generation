def calculate_perimeter(dimensions):
    return 2 * (dimensions['length'] + dimensions['width'])

if __name__ == '__main__':
    rectangle_dimensions = {'length': 15, 'width': 8}
    perimeter = calculate_perimeter(rectangle_dimensions)
    print(perimeter)