def calculate_perimeter(dimensions):
    return 2 * (dimensions['length'] + dimensions['width'])

if __name__ == '__main__':
    sample_dimensions = {'length': 10, 'width': 6}
    print(calculate_perimeter(sample_dimensions))