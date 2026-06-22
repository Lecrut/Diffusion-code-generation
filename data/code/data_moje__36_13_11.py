def trapezoid_area(base1: float, base2: float, height: float) -> float:
    return 0.5 * (base1 + base2) * height
if __name__ == '__main__':
    base1 = 5.0
    base2 = 10.0
    height = 4.0
    area = trapezoid_area(base1, base2, height)
    print(area)