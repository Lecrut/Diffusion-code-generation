RECTANGLE_SIZES = {
    'small': {'length': 3, 'width': 2},
    'medium': {'length': 5, 'width': 4},
    'large': {'length': 7, 'width': 6}
}

def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")
    return 2 * (length + width)

if __name__ == '__main__':
    size_key = 'medium'
    dimensions = RECTANGLE_SIZES[size_key]
    perimeter = calculate_rectangle_perimeter(dimensions['length'], dimensions['width'])
    print(perimeter)