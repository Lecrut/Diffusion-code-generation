def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    if diagonal1 < 0 or diagonal2 < 0:
        raise ValueError('Diagonal lengths must be non-negative.')
    return diagonal1 * diagonal2 / 2
if __name__ == '__main__':
    d1 = 10.0
    d2 = 8.0
    area = calculate_rhombus_area(d1, d2)
    print(area)