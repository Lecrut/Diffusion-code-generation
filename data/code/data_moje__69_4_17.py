from decimal import Decimal, getcontext

getcontext().prec = 50

MILES_TO_FEET = Decimal('5280')

def convert_miles_to_feet(miles):
    mile_decimal = Decimal(str(miles))
    return mile_decimal * MILES_TO_FEET

if __name__ == '__main__':
    result = convert_miles_to_feet(1.5)
    print(result)