def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rectangles = [
        {'length': 5, 'width': 3},
        {'length': 7, 'width': 2},
        {'length': 4, 'width': 6}
    ]
    
    for rectangle in rectangles:
        perimeter = calculate_perimeter(rectangle['length'], rectangle['width'])
        print(perimeter)