def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    if any(side <= 0 for side in sides):
        raise ValueError("Side lengths must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3.5, 4.2, 5.8)
        print(perimeter)
    except ValueError as e:
        print(e)