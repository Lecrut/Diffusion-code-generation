def calculate_rectangle_perimeter(dimensions):
    length = dimensions['length']
    width = dimensions['width']
    return 2 * (length + width)

if __name__ == '__main__':
    rectangle1 = {'length': 7, 'width': 4}
    perimeter1 = calculate_rectangle_perimeter(rectangle1)
    print(perimeter1)
    
    rectangle2 = {'length': 15, 'width': 8}
    perimeter2 = calculate_rectangle_perimeter(rectangle2)
    print(perimeter2)