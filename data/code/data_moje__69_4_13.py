from decimal import Decimal, getcontext
getcontext().prec = 50

def miles_to_feet(miles):
    miles_decimal = Decimal(str(miles))
    feet = miles_decimal * Decimal('5280')
    return feet
if __name__ == '__main__':
    test_miles = ['1', '0.5', '2.75', '0.123456789', '100.5']
    for m in test_miles:
        result = miles_to_feet(m)
        print(result)