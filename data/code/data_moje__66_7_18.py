from decimal import Decimal, getcontext

getcontext().prec = 50

def convert_kilometers_to_meters(kilometers: float) -> float:
    km_decimal = Decimal(str(kilometers))
    meters_decimal = km_decimal * Decimal('1000')
    return float(meters_decimal)

if __name__ == '__main__':
    result = convert_kilometers_to_meters(1.23456789)
    print(result)