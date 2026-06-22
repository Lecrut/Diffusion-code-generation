def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    if diagonal1 <= 0 or diagonal2 <= 0:
        return 0.0
    return diagonal1 * diagonal2 / 2

if __name__ == '__main__':
    diagonal1 = 6.0
    diagonal2 = 4.0
    area = calculate_rhombus_area(diagonal1, diagonal2)
    print(area)