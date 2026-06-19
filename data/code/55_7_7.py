def validate_side_length(side):
    if not isinstance(side, (int, float)) or side <= 0:
        raise ValueError("All sides must be positive numbers")

def calculate_triangle_perimeter(a, b, c):
    validate_side_length(a)
    validate_side_length(b)
    validate_side_length(c)
    
    perimeter = a + b + c
    return perimeter

if __name__ == '__main__':
    side1 = 5
    side2 = 7
    side3 = 9
    try:
        result = calculate_triangle_perimeter(side1, side2, side3)
        print(result)
    except ValueError as e:
        print(e)