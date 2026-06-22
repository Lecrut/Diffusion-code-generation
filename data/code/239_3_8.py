PERIMETER_CONSTANTS = {
    'SMALL': {'length': 5, 'width': 3},
    'MEDIUM': {'length': 10, 'width': 6},
    'LARGE': {'length': 15, 'width': 9}
}

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    size = 'MEDIUM'
    dimensions = PERIMETER_CONSTANTS[size]
    perimeter = calculate_rectangle_perimeter(dimensions['length'], dimensions['width'])
    print(perimeter)