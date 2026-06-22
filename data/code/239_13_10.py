def calculate_perimeter(dimensions):
    length = dimensions['length']
    width = dimensions['width']
    return 2 * (length + width)

if __name__ == '__main__':
    dimensions = {'length': 5, 'width': 3}
    print(calculate_perimeter(dimensions))