from decimal import Decimal, getcontext

getcontext().prec = 50

def convert_kilometers_to_meters(kilometers):
    km = Decimal(str(kilometers))
    meters = km * Decimal('1000')
    return meters

if __name__ == '__main__':
    result = convert_kilometers_to_meters(1.23456789)
    print(result)