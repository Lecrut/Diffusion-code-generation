def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    return side1 + side2 + side3

if __name__ == '__main__':
    perimeter = calculate_triangle_perimeter(3.0, 4.0, 5.0)
    print(perimeter)