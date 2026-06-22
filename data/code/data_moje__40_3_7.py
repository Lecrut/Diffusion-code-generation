from decimal import Decimal, getcontext

def calculate_surface_area(dims):
    getcontext().prec = 50
    length = Decimal(str(dims[0]))
    width = Decimal(str(dims[1]))
    height = Decimal(str(dims[2]))
    area = 2 * (length * width + width * height + height * length)
    return float(area)

if __name__ == '__main__':
    sample_dims = (2.5, 3.7, 4.2)
    result = calculate_surface_area(sample_dims)
    print(result)