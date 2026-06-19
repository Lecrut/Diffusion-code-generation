def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        return 'Invalid input: Length and width must be positive numbers.'
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    rectangles = [(10, 5), (7, 3), (-1, 4), (8, 0)]
    for length, width in rectangles:
        result = calculate_perimeter(length, width)
        print(result)