from decimal import Decimal, getcontext

def miles_to_feet(miles):
    getcontext().prec = 50
    miles_decimal = Decimal(str(miles))
    feet_decimal = miles_decimal * Decimal('5280')
    return feet_decimal

if __name__ == '__main__':
    result = miles_to_feet(1.5)
    print(result)