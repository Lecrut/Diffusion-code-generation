import math

def trapezoid_area(base1: float, base2: float, height: float) -> float:
    if height <= 0:
        raise ValueError("Height must be positive.")
    if base1 < 0 or base2 < 0:
        raise ValueError("Bases must be non-negative.")
    return (base1 + base2) * height / 2.0

if __name__ == '__main__':
    b1 = 5.0
    b2 = 7.0
    h = 4.0
    area = trapezoid_area(b1, b2, h)
    print(area)