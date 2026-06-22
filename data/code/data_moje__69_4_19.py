from decimal import Decimal, getcontext

getcontext().prec = 50

MILES_TO_FEET = Decimal('5280')

def miles_to_feet(miles):
    miles_decimal = Decimal(str(miles))
    return miles_decimal * MILES_TO_FEET

if __name__ == '__main__':
    miles_value = 1.5
    result = miles_to_feet(miles_value)
    print(result)