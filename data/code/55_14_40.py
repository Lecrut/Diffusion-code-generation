def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    if not all(isinstance(s, (int, float)) for s in sides):
        raise ValueError("All sides must be numbers")
    if any(s <= 0 for s in sides):
        raise ValueError("All sides must be positive numbers")
    return sum(sides)

if __name__ == '__main__':
    side_a = 7
    side_b = 10
    side_c = 5
    triangle_perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
    print(triangle_perimeter)