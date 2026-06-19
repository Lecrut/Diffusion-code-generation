MINIMUM_SIDE_LENGTH = 0.1

def validate_side_length(side):
    if side <= MINIMUM_SIDE_LENGTH:
        raise ValueError("Side length must be greater than {}.".format(MINIMUM_SIDE_LENGTH))

def validate_triangle_sides(a, b, c):
    validate_side_length(a)
    validate_side_length(b)
    validate_side_length(c)
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")

def calculate_perimeter(a, b, c):
    validate_triangle_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_perimeter(3.5, 4.2, 5.1)
        print(perimeter)
    except ValueError as e:
        print(e)