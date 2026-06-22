from decimal import Decimal, getcontext

getcontext().prec = 50

def calculate_surface_area(dimensions):
    length = Decimal(str(dimensions[0]))
    width = Decimal(str(dimensions[1]))
    height = Decimal(str(dimensions[2]))
    area = 2 * (length * width + length * height + width * height)
    return area

if __name__ == '__main__':
    sample_dimensions = (1.5, 2.25, 3.333)
    result = calculate_surface_area(sample_dimensions)
    print(result)