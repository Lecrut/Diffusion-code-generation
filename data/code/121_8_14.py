from decimal import Decimal, getcontext
DECIMAL_PRECISION = 50

def set_decimal_precision():
    getcontext().prec = DECIMAL_PRECISION

def compare_decimals(a, b):
    return a == b
if __name__ == '__main__':
    set_decimal_precision()
    value1 = Decimal('0.1234567890123456789012345678901234567890123456789')
    value2 = Decimal('0.12345678901234567890123456789012345678901234567890')
    value3 = Decimal('0.12345678901234567890123456789012345678901234567891')
    print(compare_decimals(value1, value2))
    print(compare_decimals(value1, value3))