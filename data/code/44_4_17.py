def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rectangles = [
        (10, 5),
        (7, 3),
        (8, 12)
    ]
    
    for length, width in rectangles:
        if length > 0 and width > 0:
            perimeter = calculate_perimeter(length, width)
            print(f"The perimeter of a rectangle with length {length} and width {width} is: {perimeter}")
        else:
            print("Invalid input: Length and width must be positive numbers.")