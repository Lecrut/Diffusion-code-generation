RECTANGLE_DIMENSIONS = {'length': 5, 'width': 3}

def calculate_perimeter(dimensions):
    return 2 * (dimensions['length'] + dimensions['width'])

if __name__ == '__main__':
    print(calculate_perimeter(RECTANGLE_DIMENSIONS))