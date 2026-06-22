def trapezoid_area(base1: float, base2: float, height: float) -> float:
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    print(trapezoid_area(5, 7, 4))