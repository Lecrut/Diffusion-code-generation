def calculate_triangle_perimeter(side1, side2, side3):
    if not isinstance(side1, (int, float)) or not isinstance(side2, (int, float)) or not isinstance(side3, (int, float)):
        raise TypeError("All side lengths must be numeric types.")
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("All side lengths must be positive.")
    if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        raise ValueError("The given sides do not form a valid triangle.")
    return side1 + side2 + side3

if __name__ == '__main__':
    result = calculate_triangle_perimeter(3, 4, 5)
    print(result)