def calculate_perimeter(dimensions):
    length = dimensions.get('length', 0)
    width = dimensions.get('width', 0)
    return 2 * (length + width)

if __name__ == '__main__':
    rectangle_properties = {'length': 6, 'width': 2}
    perimeter = calculate_perimeter(rectangle_properties)
    print(perimeter)