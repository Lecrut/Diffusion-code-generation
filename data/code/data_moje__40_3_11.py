from decimal import Decimal, getcontext

def calculate_surface_area(dimensions):
    length, width, height = map(Decimal, dimensions)
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    sample_dimensions = (12.5, 7.8, 3.2)
    result = calculate_surface_area(sample_dimensions)
    print(result)