from decimal import Decimal

def miles_to_feet(miles):
    return Decimal(miles) * Decimal('5280')

if __name__ == '__main__':
    sample_miles = [Decimal('1'), Decimal('1.5'), Decimal('0.123456789'), Decimal('100')]
    for m in sample_miles:
        print(miles_to_feet(m))