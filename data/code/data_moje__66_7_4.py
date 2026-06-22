import decimal
from decimal import Decimal

def km_to_m(kilometers):
    if not isinstance(kilometers, (int, float, Decimal, str)):
        raise TypeError("Input must be a numeric type or string")
    
    ctx = decimal.getcontext()
    original_prec = ctx.prec
    ctx.prec = 50
    
    try:
        km_value = Decimal(str(kilometers))
        conversion_factor = Decimal('1000')
        result = km_value * conversion_factor
        return result
    finally:
        ctx.prec = original_prec

if __name__ == '__main__':
    sample_km = '3.14159265358979323846'
    converted_value = km_to_m(sample_km)
    print(converted_value)