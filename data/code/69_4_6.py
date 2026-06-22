from decimal import Decimal

def miles_to_feet(miles):
    conversion_factor = Decimal('5280')
    miles_decimal = Decimal(str(miles))
    return miles_decimal * conversion_factor

if __name__ == '__main__':
    sample_miles = 1.5
    result = miles_to_feet(sample_miles)
    print(result)