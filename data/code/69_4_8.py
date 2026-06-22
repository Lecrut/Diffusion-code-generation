import decimal

def miles_to_feet(miles):
    d_miles = decimal.Decimal(miles)
    return d_miles * decimal.Decimal(5280)

if __name__ == '__main__':
    result = miles_to_feet("1.5")
    print(result)