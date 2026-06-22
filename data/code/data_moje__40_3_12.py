from decimal import Decimal, getcontext

getcontext().prec = 50

def calculate_surface_area(dimensions: tuple) -> Decimal:
    length = Decimal(str(dimensions[0]))
    width = Decimal(str(dimensions[1]))
    height = Decimal(str(dimensions[2]))

    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")

    area = 2 * (length * width + width * height + height * length)
    return area

if __name__ == '__main__':
    sample_dims = (3.14, 2.71, 1.618)
    result = calculate_surface_area(sample_dims)
    print(result)