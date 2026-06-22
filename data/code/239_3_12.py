def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    dimensions = {'length': 10, 'width': 5}
    perimeter = calculate_rectangle_perimeter(dimensions['length'], dimensions['width'])
    print(perimeter)