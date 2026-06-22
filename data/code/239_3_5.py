def calculate_rectangle_perimeter(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Both length and width must be numbers.")
    
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values.")
    
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length = 10
        width = 5
        perimeter = calculate_rectangle_perimeter(length, width)
        print(perimeter)
    except ValueError as e:
        print(e)