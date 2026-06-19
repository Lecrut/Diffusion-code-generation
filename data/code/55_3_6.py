def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 3.0
    side2 = 4.0
    side3 = 5.0
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)