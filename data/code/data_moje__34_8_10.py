import decimal

def calculate_cylinder_surface_area(radius, height, precision=50):
    decimal.getcontext().prec = precision
    r = decimal.Decimal(str(radius))
    h = decimal.Decimal(str(height))
    pi = decimal.Decimal('3.14159265358979323846264338327950288419716939937510')
    lateral_area = 2 * pi * r * h
    base_area = pi * r * r
    total_area = lateral_area + 2 * base_area
    return total_area

if __name__ == '__main__':
    sample_radius = 5.5
    sample_height = 10.2
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)