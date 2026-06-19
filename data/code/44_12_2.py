def compute_perimeter(dimensions):
    return 2 * (dimensions['length'] + dimensions['width'])

if __name__ == '__main__':
    rectangle_dimensions = {'length': 8, 'width': 4}
    perimeter = compute_perimeter(rectangle_dimensions)
    print(perimeter)