def calculate_triangle_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    side1 = 6.0
    side2 = 7.5
    side3 = 9.0
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)