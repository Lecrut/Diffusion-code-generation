def compute_rhombus_area(d1: float, d2: float) -> float:
    return 0.5 * d1 * d2

if __name__ == '__main__':
    d1 = 10.0
    d2 = 8.0
    area = compute_rhombus_area(d1, d2)
    print(area)