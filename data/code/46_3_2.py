def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c
if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    try:
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(f"The perimeter of a triangle with sides {side1}, {side2}, and {side3} is: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}")
    side4 = 1
    side5 = 2
    side6 = 10
    try:
        perimeter = calculate_triangle_perimeter(side4, side5, side6)
        print(f"The perimeter of a triangle with sides {side4}, {side5}, and {side6} is: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}")
    side7 = -1
    side8 = 4
    side9 = 5
    try:
        perimeter = calculate_triangle_perimeter(side7, side8, side9)
        print(f"The perimeter of a triangle with sides {side7}, {side8}, and {side9} is: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}")