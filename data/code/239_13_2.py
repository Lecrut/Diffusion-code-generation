def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    dimensions = {'length': 5, 'width': 3}
    length = dimensions['length']
    width = dimensions['width']
    print(calculate_perimeter(length, width))