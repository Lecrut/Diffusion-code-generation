from decimal import Decimal, getcontext

def calculate_surface_area(dimensions):
    length, width, height = dimensions
    getcontext().prec = 50
    l = Decimal(str(length))
    w = Decimal(str(width))
    h = Decimal(str(height))
    surface_area = 2 * (l * w + w * h + h * l)
    return float(surface_area)

if __name__ == '__main__':
    sample_dimensions = (1.5, 2.5, 3.5)
    result = calculate_surface_area(sample_dimensions)
    print(result)