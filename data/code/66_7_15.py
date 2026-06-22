from decimal import Decimal, getcontext

def kilometers_to_meters(kilometers):
    getcontext().prec = 50
    km_decimal = Decimal(str(kilometers))
    return km_decimal * Decimal('1000')

if __name__ == '__main__':
    result = kilometers_to_meters(1.23456789012345678901234567890)
    print(result)
    result2 = kilometers_to_meters(0.000001)
    print(result2)