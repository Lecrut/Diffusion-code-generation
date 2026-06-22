def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    if not all(isinstance(s, (int, float)) for s in sides):
        raise ValueError("All sides must be numbers")
    if any(s <= 0 for s in sides):
        raise ValueError("All sides must be positive numbers")
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    side1_length = 7
    side2_length = 10
    side3_length = 5
    triangle_perimeter = calculate_triangle_perimeter(side1_length, side2_length, side3_length)
    print(triangle_perimeter)