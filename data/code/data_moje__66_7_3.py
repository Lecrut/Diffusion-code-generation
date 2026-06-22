from decimal import Decimal, getcontext

getcontext().prec = 50

def convert_km_to_m(kilometers):
    if isinstance(kilometers, (int, float)):
        kilometers = Decimal(str(kilometers))
    meters = kilometers * Decimal('1000')
    return meters

if __name__ == '__main__':
    sample_km = Decimal('123.456789012345678901234567890')
    result = convert_km_to_m(sample_km)
    print(result)
    
    sample_km_2 = Decimal('0.000000001')
    result_2 = convert_km_to_m(sample_km_2)
    print(result_2)