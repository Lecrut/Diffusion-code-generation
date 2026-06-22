def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    return side1 + side2 + side3

if __name__ == '__main__':
    a = 3.0
    b = 4.0
    c = 5.0
    perimeter = calculate_triangle_perimeter(a, b, c)
    print(perimeter)