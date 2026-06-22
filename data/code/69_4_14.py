from decimal import Decimal, getcontext

getcontext().prec = 28

def miles_to_feet(miles):
    decimal_miles = Decimal(str(miles))
    return decimal_miles * Decimal('5280')

if __name__ == '__main__':
    result = miles_to_feet(1.5)
    print(result)