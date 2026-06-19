def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    dimensions = {'length': 10, 'width': 5}
    perimeter = calculate_perimeter(dimensions['length'], dimensions['width'])
    print(f"Length: {dimensions['length']}")
    print(f"Width: {dimensions['width']}")
    print(f"Perimeter: {perimeter}")