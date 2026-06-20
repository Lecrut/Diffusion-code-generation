def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    return side_a + side_b + side_c

if __name__ == '__main__':
    a = 3.0
    b = 4.0
    c = 5.0
    perimeter = calculate_triangle_perimeter(a, b, c)
    print(perimeter)