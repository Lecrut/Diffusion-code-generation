import math

_RADIi_UNITS = {
    "m": 1.0,
    "cm": 0.01,
    "in": 0.0254
}

def circle_area(radius, unit="m"):
    factor = _RADIi_UNITS.get(unit, 1.0)
    return math.pi * (radius * factor) ** 2

if __name__ == '__main__':
    print(circle_area(10, "cm"))
    print(circle_area(2, "in"))