from decimal import Decimal, getcontext

def kilometers_to_meters(kilometers):
    getcontext().prec = 50
    km = Decimal(str(kilometers))
    meters = km * Decimal('1000')
    return meters

if __name__ == '__main__':
    sample_km = 123.45678901234567890123456789
    result = kilometers_to_meters(sample_km)
    print(result)