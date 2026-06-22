def compute_rhombus_area(d1: float, d2: float) -> float:
    return 0.5 * d1 * d2

if __name__ == '__main__':
    diagonal1 = 10.0
    diagonal2 = 8.0
    area = compute_rhombus_area(diagonal1, diagonal2)
    print(area)