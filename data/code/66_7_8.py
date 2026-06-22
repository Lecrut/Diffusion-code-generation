from decimal import Decimal, getcontext

def kilometers_to_meters(kilometers):
    getcontext().prec = 50
    km = Decimal(str(kilometers))
    meters = km * Decimal(1000)
    return meters

if __name__ == '__main__':
    result = kilometers_to_meters(1.23456789012345678901234567890)
    print(result)