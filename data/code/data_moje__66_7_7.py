from decimal import Decimal, getcontext

def km_to_m(km):
    if not isinstance(km, Decimal):
        km = Decimal(str(km))
    getcontext().prec = 50
    return km * Decimal('1000')

if __name__ == '__main__':
    sample_km = Decimal('123.456789012345678901234567890')
    result = km_to_m(sample_km)
    print(result)