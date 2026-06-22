import decimal

def calculate_surface_area(dimensions):
    context = decimal.getcontext()
    context.prec = 50
    l, w, h = map(decimal.Decimal, dimensions)
    area = 2 * (l * w + l * h + w * h)
    return float(area)

if __name__ == '__main__':
    sample_dimensions = (1.5, 2.5, 3.7)
    result = calculate_surface_area(sample_dimensions)
    print(result)