from decimal import Decimal, getcontext

def miles_to_feet(miles):
    getcontext().prec = 28
    decimal_miles = Decimal(str(miles))
    feet = decimal_miles * Decimal(5280)
    return feet

if __name__ == '__main__':
    result = miles_to_feet(1.5)
    print(result)