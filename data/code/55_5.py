def calculate_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c
if __name__ == '__main__':
    side_a = 3.0
    side_b = 4.0
    side_c = 5.0
    perimeter = calculate_perimeter(side_a, side_b, side_c)
    print(perimeter)