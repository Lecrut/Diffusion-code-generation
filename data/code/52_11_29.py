MIN_DIMENSION = 0.1

def calculate_rectangle_area(length, width):
    if length <= MIN_DIMENSION or width <= MIN_DIMENSION:
        raise ValueError("Length and width must be greater than the minimum dimension.")
    return length * width

if __name__ == '__main__':
    sample_length = 6.2
    sample_width = 4.8
    area = calculate_rectangle_area(sample_length, sample_width)
    print(area)