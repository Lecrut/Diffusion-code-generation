MIN_SIDE_LENGTH = 0

def calculate_triangle_perimeter(a, b, c):
    if a <= MIN_SIDE_LENGTH or b <= MIN_SIDE_LENGTH or c <= MIN_SIDE_LENGTH:
        raise ValueError("Side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)