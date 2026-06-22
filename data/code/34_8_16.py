import decimal
from decimal import Decimal

def calculate_cylinder_surface_area(radius, height):
    precision_context = decimal.getcontext().copy()
    precision_context.prec = 50
    decimal.setcontext(precision_context)
    r = Decimal(str(radius))
    h = Decimal(str(height))
    two = Decimal('2')
    pi = Decimal('3.14159265358979323846264338327950288419716939937510')
    lateral_area = two * pi * r * h
    base_area = pi * r * r
    total_area = lateral_area + two * base_area
    return total_area

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)