from decimal import Decimal, getcontext

def validate_division(dividend, divisor):
    if not isinstance(dividend, Decimal) or not isinstance(divisor, Decimal):
        raise ValueError("Both dividend and divisor must be instances of Decimal.")
    if divisor == Decimal('0'):
        raise ZeroDivisionError("Divisor cannot be zero.")

def divide_decimals():
    getcontext().prec = 50
    dividend = Decimal('1.234567890123456789012345678901234567890123456789')
    divisor = Decimal('2.345678901234567890123456789012345678901234567890')
    
    validate_division(dividend, divisor)
    result = dividend / divisor
    return result

if __name__ == '__main__':
    print(divide_decimals())