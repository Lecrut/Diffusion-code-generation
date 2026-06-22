import math

def trapezoid_area(base1: float, base2: float, height: float) -> float:
    if height < 0:
        raise ValueError("Height cannot be negative")
    if base1 < 0 or base2 < 0:
        raise ValueError("Bases cannot be negative")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    result = trapezoid_area(5.0, 7.0, 4.0)
    print(result)