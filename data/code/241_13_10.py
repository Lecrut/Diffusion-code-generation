def rectangle_area(dimensions):
    length, width = dimensions
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

if __name__ == '__main__':
    sample_dimensions = (5, 3)
    try:
        area = rectangle_area(sample_dimensions)
        print(area)
    except ValueError as e:
        print(e)