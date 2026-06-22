def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        return None
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    rectangles = [(10, 5), (7, 3), (4.5, 2.8), (-1, 5)]
    for length, width in rectangles:
        result = calculate_perimeter(length, width)
        if result is not None:
            print(f"The perimeter of rectangle with length {length} and width {width} is: {result}")
        else:
            print(f"Invalid input: Length and width must be positive numbers.")