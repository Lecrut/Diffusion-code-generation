from decimal import Decimal, getcontext

getcontext().prec = 50

def km_to_m(km_value):
    km_decimal = Decimal(str(km_value))
    meters = km_decimal * Decimal('1000')
    return meters

if __name__ == '__main__':
    sample_values = [1.5, 0.123456789, 1000.0, 0.001]
    for val in sample_values:
        result = km_to_m(val)
        print(result)