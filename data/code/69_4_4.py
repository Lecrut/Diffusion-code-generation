from decimal import Decimal, getcontext

getcontext().prec = 28

def miles_to_feet(miles):
    miles_decimal = Decimal(str(miles))
    feet_per_mile = Decimal('5280')
    feet = miles_decimal * feet_per_mile
    return feet

if __name__ == '__main__':
    sample_miles = [1, 2.5, 0.123456789, 1000]
    for m in sample_miles:
        result = miles_to_feet(m)
        print(result)