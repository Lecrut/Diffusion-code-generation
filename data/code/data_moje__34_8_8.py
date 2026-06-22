import math
from decimal import Decimal, getcontext

getcontext().prec = 50

def cylinder_surface_area(radius: float, height: float) -> float:
    r = Decimal(str(radius))
    h = Decimal(str(height))
    pi = Decimal(str(math.pi))
    area = 2 * pi * r * (r + h)
    return float(area)

if __name__ == '__main__':
    result = cylinder_surface_area(3.5, 10.2)
    print(result)