def rectangle_area(dimensions):
    length, width = dimensions
    return length * width

if __name__ == '__main__':
    sample_dimensions = (5, 3)
    print(rectangle_area(sample_dimensions))