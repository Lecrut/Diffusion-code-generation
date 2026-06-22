def calculate_perimeter(dimensions):
    return 2 * (dimensions['length'] + dimensions['width'])

if __name__ == '__main__':
    rectangle_properties = {'length': 8, 'width': 4}
    perimeter_result = calculate_perimeter(rectangle_properties)
    print(perimeter_result)