from decimal import Decimal, getcontext

def calculate_surface_area(dimensions):
    getcontext().prec = 50
    length = Decimal(str(dimensions[0]))
    width = Decimal(str(dimensions[1]))
    height = Decimal(str(dimensions[2]))
    area = 2 * (length * width + width * height + height * length)
    return area

if __name__ == '__main__':
    sample_dimensions = (1.5, 2.7, 3.9)
    result = calculate_surface_area(sample_dimensions)
    print(result)