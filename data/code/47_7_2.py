def calculate_area(dimensions):
    return dimensions['length'] * dimensions['width']

if __name__ == '__main__':
    sample_dimensions = {'length': 7, 'width': 4}
    area = calculate_area(sample_dimensions)
    print(area)