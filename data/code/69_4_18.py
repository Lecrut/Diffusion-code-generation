from decimal import Decimal

def miles_to_feet(miles):
    feet_per_mile = Decimal('5280')
    return Decimal(str(miles)) * feet_per_mile

if __name__ == '__main__':
    sample_miles = [Decimal('1'), Decimal('0.5'), Decimal('10.123456789')]
    for m in sample_miles:
        print(miles_to_feet(m))