def calculate_triangle_perimeter(a, b, c):
    sides = [a, b, c]
    for side in sides:
        if side <= 0:
            raise ValueError("Side lengths must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    try:
        side1 = 5
        side2 = 6
        side3 = 7
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)