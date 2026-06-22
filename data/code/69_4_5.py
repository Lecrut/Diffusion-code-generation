from decimal import Decimal

def miles_to_feet(miles):
    decimal_miles = Decimal(str(miles))
    feet = decimal_miles * Decimal('5280')
    return float(feet)

if __name__ == '__main__':
    result = miles_to_feet(1.5)
    print(result)