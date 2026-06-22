from decimal import Decimal, getcontext

def calculate_cylinder_surface_area(radius_str: str, height_str: str, precision: int = 50) -> Decimal:
    getcontext().prec = precision
    radius = Decimal(radius_str)
    height = Decimal(height_str)
    pi = getcontext().decimal_factory.pi()
    lateral_area = 2 * pi * radius * height
    base_area = pi * radius ** 2
    total_surface_area = lateral_area + 2 * base_area
    return total_surface_area

if __name__ == '__main__':
    sample_radius = "5.25"
    sample_height = "10.75"
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)