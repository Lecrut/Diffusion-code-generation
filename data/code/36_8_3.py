import math

def trapezoid_area(base1: float, base2: float, height: float) -> float:
    return (base1 + base2) * height / 2.0

if __name__ == '__main__':
    b1 = 5.0
    b2 = 7.0
    h = 4.0
    area = trapezoid_area(b1, b2, h)
    print(area)