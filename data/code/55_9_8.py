def calculate_triangle_perimeter(a, b, c):
    if not all(side > 0 for side in (a, b, c)):
        raise ValueError("All side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        side1 = 7
        side2 = 8
        side3 = 9
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)