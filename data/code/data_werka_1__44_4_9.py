def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    rectangles = [
        (10, 5),
        (7, 3),
        (15, 8)
    ]
    
    for length, width in rectangles:
        if length > 0 and width > 0:
            print(calculate_perimeter(length, width))
        else:
            print("Invalid input: Length and width must be positive numbers.")