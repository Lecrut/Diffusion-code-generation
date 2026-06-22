import decimal

def miles_to_feet(miles):
    ctx = decimal.getcontext()
    ctx.prec = 50
    decimal_miles = decimal.Decimal(str(miles))
    feet_per_mile = decimal.Decimal('5280')
    result = decimal_miles * feet_per_mile
    return result

if __name__ == '__main__':
    sample_value = 3.5
    output = miles_to_feet(sample_value)
    print(output)