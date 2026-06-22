from decimal import Decimal, getcontext

def calculate_cylinder_surface_area(radius, height):
    getcontext().prec = 50
    r = Decimal(str(radius))
    h = Decimal(str(height))
    pi = Decimal(
        '3.14159265358979323846264338327950288419716939937510'
    )
    base_area = pi * r ** 2
    lateral_area = 2 * pi * r * h
    total_area = 2 * base_area + lateral_area
    return float(total_area)

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)