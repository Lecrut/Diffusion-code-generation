import math
from decimal import Decimal, getcontext

getcontext().prec = 28

def cylinder_surface_area(radius, height):
    r = Decimal(str(radius))
    h = Decimal(str(height))
    pi = Decimal(str(math.pi))
    lateral_area = Decimal('2') * pi * r * h
    base_area = Decimal('2') * pi * r * r
    total_area = lateral_area + base_area
    return total_area

if __name__ == '__main__':
    r_val = 5.0
    h_val = 10.0
    result = cylinder_surface_area(r_val, h_val)
    print(result)