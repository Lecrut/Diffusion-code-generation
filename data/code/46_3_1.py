def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c
if __name__ == '__main__':
    try:
        side1 = 3
        side2 = 4
        side3 = 5
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(f"The perimeter of a triangle with sides {side1}, {side2}, and {side3} is: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        side1 = -1
        side2 = 4
        side3 = 5
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        side1 = 1
        side2 = 2
        side3 = 10
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
    except ValueError as e:
        print(f"Error: {e}")