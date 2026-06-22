import decimal
from decimal import Decimal, getcontext

getcontext().prec = 50

def calculate_cylinder_surface_area(radius, height):
    radius_dec = Decimal(str(radius))
    height_dec = Decimal(str(height))
    pi_dec = Decimal('3.14159265358979323846264338327950288419716939937510')
    lateral_area = 2 * pi_dec * radius_dec * height_dec
    base_area = pi_dec * radius_dec ** 2
    total_area = lateral_area + 2 * base_area
    return total_area

if __name__ == '__main__':
    sample_radius = 5.5
    sample_height = 10.25
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)