from decimal import Decimal

def miles_to_feet(miles):
    feet_per_mile = Decimal('5280')
    return Decimal(str(miles)) * feet_per_mile

if __name__ == '__main__':
    print(miles_to_feet(1))
    print(miles_to_feet(0.5))
    print(miles_to_feet(123.456))