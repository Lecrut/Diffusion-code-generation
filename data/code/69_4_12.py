from decimal import Decimal

def miles_to_feet(miles):
    mile_in_feet = Decimal('5280')
    return Decimal(str(miles)) * mile_in_feet

if __name__ == '__main__':
    result = miles_to_feet(1.5)
    print(result)