def trapezoid_area(base1: float, base2: float, height: float) -> float:
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    print(trapezoid_area(5.0, 7.0, 4.0))