def calculate_triangle_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    side_length_1 = 6.0
    side_length_2 = 8.0
    side_length_3 = 10.0
    perimeter = calculate_triangle_perimeter(side_length_1, side_length_2, side_length_3)
    print(perimeter)