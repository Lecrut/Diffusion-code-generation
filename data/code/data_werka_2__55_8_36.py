def validate_side_length(side):
    if side <= 0:
        raise ValueError("Side lengths must be positive numbers.")

def calculate_triangle_perimeter(a, b, c):
    sides = [a, b, c]
    for side in sides:
        validate_side_length(side)
    return sum(sides)

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(9, 12, 15)
        print(perimeter)
    except ValueError as e:
        print(e)