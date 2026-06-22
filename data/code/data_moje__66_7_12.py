from decimal import Decimal, getcontext

def kilometers_to_meters(km_value):
    getcontext().prec = 50
    km = Decimal(str(km_value))
    meters = km * Decimal('1000')
    return meters

if __name__ == '__main__':
    sample_km = 1.5
    result = kilometers_to_meters(sample_km)
    print(result)