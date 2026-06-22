from decimal import Decimal

MILES_TO_FEET = Decimal(5280)

def miles_to_feet(miles):
    return Decimal(str(miles)) * MILES_TO_FEET

if __name__ == '__main__':
    sample_miles = [1, 2.5, 10, 0.1, 100.125]
    for m in sample_miles:
        print(miles_to_feet(m))