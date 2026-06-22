def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    return diagonal1 * diagonal2 / 2

if __name__ == '__main__':
    d1 = 10.0
    d2 = 5.0
    area = calculate_rhombus_area(d1, d2)
    print(area)