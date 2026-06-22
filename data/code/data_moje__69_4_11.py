import decimal

decimal.getcontext().prec = 50

def miles_to_feet(miles):
    conversion_factor = decimal.Decimal('5280')
    miles_decimal = decimal.Decimal(str(miles))
    return miles_decimal * conversion_factor

if __name__ == '__main__':
    sample_miles = 2.5
    result = miles_to_feet(sample_miles)
    print(result)
    another_sample = '10.0000001'
    print(miles_to_feet(another_sample))