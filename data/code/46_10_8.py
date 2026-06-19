def is_valid_triangle_side(side):
    return side > 0

def calculate_triangle_perimeter(a, b, c):
    if not (is_valid_triangle_side(a) and is_valid_triangle_side(b) and is_valid_triangle_side(c)):
        raise ValueError("All side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        side_a = 7.0
        side_b = 10.0
        side_c = 5.0
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(e)