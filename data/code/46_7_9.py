def calculate_triangle_perimeter(a: float, b: float, c: float) -> float:
    return sum([a, b, c])

if __name__ == '__main__':
    side1 = 7.0
    side2 = 9.5
    side3 = 6.3
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)