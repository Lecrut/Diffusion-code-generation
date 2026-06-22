from decimal import Decimal, InvalidOperation

def km_to_m(kilometers):
    if isinstance(kilometers, float):
        kilometers = Decimal(str(kilometers))
    elif not isinstance(kilometers, Decimal):
        kilometers = Decimal(kilometers)
    return float(kilometers * 1000)

if __name__ == '__main__':
    sample_values = [1.0, 0.0, -5.5, 123.456789, 1e-10, 1e10]
    for val in sample_values:
        print(km_to_m(val))