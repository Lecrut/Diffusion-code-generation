RECTANGLE_DIMENSIONS = {
    'length': 15,
    'width': 8
}

def calculate_perimeter(dimensions):
    return 2 * (dimensions['length'] + dimensions['width'])

if __name__ == '__main__':
    perimeter = calculate_perimeter(RECTANGLE_DIMENSIONS)
    print(perimeter)