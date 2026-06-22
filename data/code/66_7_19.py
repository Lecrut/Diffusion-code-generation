from decimal import Decimal, getcontext

getcontext().prec = 28

def kilometers_to_meters(km):
    km_decimal = Decimal(str(km))
    return km_decimal * Decimal('1000')

if __name__ == '__main__':
    result = kilometers_to_meters(1.2345678901234567890123456789)
    print(result)