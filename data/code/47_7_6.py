def calculate_area(dimensions):
    return dimensions['length'] * dimensions['width']

if __name__ == '__main__':
    sample_dimensions = {'length': 9, 'width': 6}
    area = calculate_area(sample_dimensions)
    print(area)