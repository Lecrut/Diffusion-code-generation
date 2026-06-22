import math
_UNIT_FACTORS = {"m": 1.0, "cm": 0.01, "mm": 0.001}
def circle_area(radius, unit="m"):
    return math.pi * (radius * _UNIT_FACTORS.get(unit, 1.0)) ** 2
if __name__ == '__main__':
    print(circle_area(10, "cm"))
    print(circle_area(3, "m"))