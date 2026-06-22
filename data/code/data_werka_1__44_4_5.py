def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rectangles = [
        (5, 3),
        (7, 2),
        (4, 6)
    ]
    
    for length, width in rectangles:
        perimeter = calculate_perimeter(length, width)
        print(perimeter)