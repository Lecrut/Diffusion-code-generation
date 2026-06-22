def compute_perimeter(dimensions):
    return 2 * (dimensions['length'] + dimensions['width'])

if __name__ == '__main__':
    rectangle_properties = {'length': 6, 'width': 2}
    perimeter_value = compute_perimeter(rectangle_properties)
    print(perimeter_value)