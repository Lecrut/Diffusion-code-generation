def calculate_triangle_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    side_a = 7.0
    side_b = 9.5
    side_c = 12.3
    perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
    print(perimeter)