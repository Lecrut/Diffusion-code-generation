def trapezoid_area(base1: float, base2: float, height: float) -> float:
    return (base1 + base2) * height / 2

if __name__ == '__main__':
    b1: float = 5.0
    b2: float = 10.0
    h: float = 4.0
    result: float = trapezoid_area(b1, b2, h)
    print(result)