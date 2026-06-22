from decimal import Decimal, getcontext

getcontext().prec = 50

def calculate_surface_area(dims):
    width, height, depth = (Decimal(str(d)) for d in dims)
    return 2 * (width * height + height * depth + depth * width)

if __name__ == '__main__':
    sample_dims = (3.5, 2.1, 4.8)
    result = calculate_surface_area(sample_dims)
    print(result)