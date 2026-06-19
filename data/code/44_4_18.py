def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    rectangles = [(7, 3), (4.5, 6.2), (10, 10), (0, 5), (-3, 4)]
    for length, width in rectangles:
        if length > 0 and width > 0:
            perimeter = calculate_perimeter(length, width)
            print(f'The perimeter of a rectangle with length {length} and width {width} is: {perimeter}')
        else:
            print(f'Invalid input: Length and width must be positive numbers. Got length={length}, width={width}.')