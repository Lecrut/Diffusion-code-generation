from decimal import Decimal, getcontext, ROUND_HALF_EVEN

getcontext().prec = 50

def calculate_surface_area(dimensions):
    width = Decimal(str(dimensions[0]))
    height = Decimal(str(dimensions[1]))
    depth = Decimal(str(dimensions[2]))
    
    return 2 * (width * height + width * depth + height * depth)

if __name__ == '__main__':
    sample_dimensions = (1.5, 2.3, 3.7)
    result = calculate_surface_area(sample_dimensions)
    print(result)