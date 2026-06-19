def validate_dimensions(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive.")

def calculate_perimeter(length, width):
    validate_dimensions(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length = 6
        width = 4
        perimeter1 = calculate_perimeter(length, width)
        print(perimeter1)
        
        length = 9
        width = 3
        perimeter2 = calculate_perimeter(length, width)
        print(perimeter2)
    except ValueError as e:
        print(e)