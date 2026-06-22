def calculate_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    TRIANGLE_SIDE_A = 3.5
    TRIANGLE_SIDE_B = 4.2
    TRIANGLE_SIDE_C = 5.1
    perimeter_result = calculate_perimeter(TRIANGLE_SIDE_A, TRIANGLE_SIDE_B, TRIANGLE_SIDE_C)
    print(perimeter_result)