def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rectangle_dimensions = {'length': 6, 'width': 4}
    length = rectangle_dimensions['length']
    width = rectangle_dimensions['width']
    perimeter = calculate_perimeter(length, width)
    print(perimeter)