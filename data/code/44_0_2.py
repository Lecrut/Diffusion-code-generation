RECTANGLE_DIMENSIONS = {
    'sample1': {'length': 7, 'width': 4},
    'sample2': {'length': 6, 'width': 2}
}

def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")
    return 2 * (length + width)

if __name__ == '__main__':
    sample_key = 'sample1'
    dimensions = RECTANGLE_DIMENSIONS[sample_key]
    perimeter = calculate_rectangle_perimeter(dimensions['length'], dimensions['width'])
    print(perimeter)