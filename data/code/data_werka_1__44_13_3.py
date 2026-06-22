def calculate_perimeter(dimensions):
    length = dimensions['length']
    width = dimensions['width']
    return 2 * (length + width)

if __name__ == '__main__':
    rectangle_dimensions = {'length': 15, 'width': 7}
    perimeter = calculate_perimeter(rectangle_dimensions)
    print(perimeter)