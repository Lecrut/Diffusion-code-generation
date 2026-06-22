import math
from decimal import Decimal, getcontext

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    getcontext().prec = 50
    r = Decimal(str(radius))
    h = Decimal(str(height))
    pi = Decimal(str(math.pi))
    surface_area = 2 * pi * r * (r + h)
    return float(surface_area)

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)