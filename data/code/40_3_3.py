import math
from decimal import Decimal, getcontext, localcontext

def calculate_box_surface_area(dimensions):
    getcontext().prec = 50
    with localcontext() as ctx:
        ctx.prec = 50
        l = Decimal(str(dimensions[0]))
        w = Decimal(str(dimensions[1]))
        h = Decimal(str(dimensions[2]))
        area = (l * w) + (l * h) + (w * h)
        return area * Decimal(2)

if __name__ == '__main__':
    sample_dimensions = (1.5, 2.5, 3.5)
    result = calculate_box_surface_area(sample_dimensions)
    print(result)