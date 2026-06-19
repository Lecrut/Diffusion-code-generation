def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        return None
    return 2 * (length + width)
if __name__ == '__main__':
    rectangles = [(10, 5), (7, 3), (0, 4), (-2, 6)]
    for length, width in rectangles:
        perimeter = calculate_perimeter(length, width)
        if perimeter is not None:
            print(f'The perimeter of a rectangle with length {length} and width {width} is: {perimeter}')
        else:
            print(f'Invalid input: Length and width must be positive numbers for a rectangle with length {length} and width {width}.')