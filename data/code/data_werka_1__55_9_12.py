def validate_side_length(side):
    if side <= 0:
        raise ValueError(f"Side length '{side}' must be a positive number.")

def calculate_triangle_perimeter(a, b, c):
    validate_side_length(a)
    validate_side_length(b)
    validate_side_length(c)
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(6, 8, 10)
        print(perimeter)
    except ValueError as e:
        print(e)