def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    if not all(isinstance(s, (int, float)) for s in sides):
        raise ValueError("All sides must be numbers")
    if any(s <= 0 for s in sides):
        raise ValueError("All sides must be positive numbers")
    return sum(sides)

if __name__ == '__main__':
    side1 = 7
    side2 = 10
    side3 = 5
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)