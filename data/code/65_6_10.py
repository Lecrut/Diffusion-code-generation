from decimal import Decimal, getcontext

getcontext().prec = 50

def feet_to_inches(feet: float) -> float:
    decimal_feet = Decimal(str(feet))
    inches = decimal_feet * Decimal('12')
    return float(inches)

if __name__ == '__main__':
    sample_feet = 5.5
    result = feet_to_inches(sample_feet)
    print(result)