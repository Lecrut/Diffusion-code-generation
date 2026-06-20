from decimal import Decimal, getcontext

def validate_inputs(a, b):
    if not isinstance(a, Decimal) or not isinstance(b, Decimal):
        raise ValueError("Both inputs must be Decimal objects.")
    if b == Decimal('0'):
        raise ZeroDivisionError("Cannot divide by zero.")

def divide_decimals(a, b):
    getcontext().prec = 50
    validate_inputs(a, b)
    result = a / b
    return result

if __name__ == '__main__':
    sample_a = Decimal('1.234567890123456789012345678901234567890123456789')
    sample_b = Decimal('2.345678901234567890123456789012345678901234567890')
    print(divide_decimals(sample_a, sample_b))