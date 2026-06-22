def calculate_area(dimensions):
    length, width = dimensions
    return length * width

if __name__ == '__main__':
    sample_dimensions = (5, 3)
    area = calculate_area(sample_dimensions)
    print(area)