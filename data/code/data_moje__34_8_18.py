import math
from decimal import Decimal, getcontext

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    getcontext().prec = 50
    r = Decimal(str(radius))
    h = Decimal(str(height))
    two = Decimal('2')
    pi = Decimal(str(math.pi))
    area = two * pi * r * (r + h)
    return float(area)

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    result = calculate_cylinder_surface_area(radius, height)
    print(result)