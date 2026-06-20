from decimal import Decimal

def multiply_decimals(a, b):
    return Decimal(a) * Decimal(b)

if __name__ == '__main__':
    result = multiply_decimals(2.5, 4.2)
    print(result)