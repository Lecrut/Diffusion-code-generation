def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    dimensions = {'length': 10, 'width': 5}
    length = dimensions['length']
    width = dimensions['width']
    perimeter = calculate_perimeter(length, width)
    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Perimeter: {perimeter}")