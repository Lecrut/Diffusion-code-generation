def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    return 0.5 * diagonal1 * diagonal2

if __name__ == '__main__':
    diag1 = 10.0
    diag2 = 6.0
    area = calculate_rhombus_area(diag1, diag2)
    print(area)