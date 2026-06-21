def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    if any(s <= 0 for s in sides):
        raise ValueError("All sides must be positive numbers")
    return sum(sides)

if __name__ == '__main__':
    side1 = 7
    side2 = 9
    side3 = 12
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)