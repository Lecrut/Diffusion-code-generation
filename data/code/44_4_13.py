def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    rectangles = [
        {"length": 10, "width": 5},
        {"length": 7, "width": 3},
        {"length": 15, "width": 8}
    ]
    
    for rect in rectangles:
        try:
            perimeter = calculate_perimeter(rect["length"], rect["width"])
            print(f"The perimeter of a rectangle with length {rect['length']} and width {rect['width']} is: {perimeter}")
        except ValueError as e:
            print(e)