def validate_length_width(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive.")

def calculate_perimeter(length, width):
    validate_length_width(length, width)
    return 2 * (length + width)

if __name__ == '__main__':
    try:
        length1 = 6
        width1 = 4
        perimeter1 = calculate_perimeter(length1, width1)
        print(perimeter1)
        
        length2 = 9.5
        width2 = 3.2
        perimeter2 = calculate_perimeter(length2, width2)
        print(perimeter2)
    except ValueError as e:
        print(e)