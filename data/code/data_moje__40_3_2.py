from decimal import Decimal, getcontext

getcontext().prec = 50

def calculate_surface_area(dimensions):
    length = Decimal(str(dimensions[0]))
    width = Decimal(str(dimensions[1]))
    height = Decimal(str(dimensions[2]))
    surface_area = 2 * (length * width + width * height + height * length)
    return float(surface_area)

if __name__ == '__main__':
    sample_dimensions = (2.5, 3.7, 4.1)
    result = calculate_surface_area(sample_dimensions)
    print(result)