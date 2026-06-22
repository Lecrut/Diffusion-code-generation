from decimal import Decimal

MILES_TO_FEET = Decimal('5280')

def convert_miles_to_feet(miles: Decimal) -> Decimal:
    return miles * MILES_TO_FEET

if __name__ == '__main__':
    result = convert_miles_to_feet(Decimal('10'))
    print(result)