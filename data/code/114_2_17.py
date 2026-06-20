from decimal import Decimal
DECIMAL_PRECISION = 28

def multiply_decimals(a, b):
    return (Decimal(str(a)) * Decimal(str(b))).quantize(Decimal('1.' + '0' * DECIMAL_PRECISION))
if __name__ == '__main__':
    result = multiply_decimals(0.1, 0.2)
    print(result)