import math

from decimal import Decimal, getcontext

def calculate_cylinder_surface_area(radius, height):
    getcontext().prec = 50
    r = Decimal(str(radius))
    h = Decimal(str(height))
    pi = Decimal(str(math.pi))
    lateral_area = 2 * pi * r * h
    base_area = pi * r ** 2
    total_surface_area = lateral_area + 2 * base_area
    return float(total_surface_area)

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)