def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        return 'Invalid input: Length and width must be positive numbers.'
    perimeter = 2 * (length + width)
    return f'The perimeter is: {perimeter}'
if __name__ == '__main__':
    rectangles = [(15, 7), (8, 3), (0, 5), (-4, 6)]
    for length, width in rectangles:
        result = calculate_perimeter(length, width)
        print(result)