from decimal import Decimal, getcontext

getcontext().prec = 50

def kilometers_to_meters(kilometers):
    km_decimal = Decimal(str(kilometers))
    meters_decimal = km_decimal * Decimal(1000)
    return meters_decimal

if __name__ == '__main__':
    result = kilometers_to_meters(1.23456789012345)
    print(result)