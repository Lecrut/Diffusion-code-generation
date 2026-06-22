RECTANGLE_CONFIG = {
    'rectangle1': {'length': 5, 'width': 3},
    'rectangle2': {'length': 9, 'width': 4}
}

def calculate_rectangle_perimeter(length, width):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer.")
    return 2 * (length + width)

if __name__ == '__main__':
    sample_key = 'rectangle1'
    rectangle_dimensions = RECTANGLE_CONFIG[sample_key]
    perimeter = calculate_rectangle_perimeter(rectangle_dimensions['length'], rectangle_dimensions['width'])
    print(perimeter)