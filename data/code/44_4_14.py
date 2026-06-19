def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    rectangles = [
        {'length': 8, 'width': 3},
        {'length': 15, 'width': 7}
    ]
    
    for rectangle in rectangles:
        length = rectangle['length']
        width = rectangle['width']
        if length > 0 and width > 0:
            perimeter = calculate_perimeter(length, width)
            print(f"The perimeter of a rectangle with length {length} and width {width} is: {perimeter}")
        else:
            print("Invalid input: Length and width must be positive numbers.")