RECTANGLE_DIMENSIONS = {
    'length': 10,
    'width': 4
}

def calculate_perimeter(dimensions):
    return 2 * (dimensions['length'] + dimensions['width'])

if __name__ == '__main__':
    perimeter = calculate_perimeter(RECTANGLE_DIMENSIONS)
    print(perimeter)