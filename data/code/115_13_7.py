from decimal import Decimal, getcontext

def validate_inputs(a, b):
    if not isinstance(a, Decimal) or not isinstance(b, Decimal):
        raise ValueError("Both inputs must be Decimal objects.")
    if b == Decimal('0'):
        raise ValueError("Cannot divide by zero.")

def perform_division(a, b):
    getcontext().prec = 50
    result = a / b
    return result

def main():
    try:
        a = Decimal('1.234567890123456789012345678901234567890123456789')
        b = Decimal('2.345678901234567890123456789012345678901234567890')
        validate_inputs(a, b)
        result = perform_division(a, b)
        print(result)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()