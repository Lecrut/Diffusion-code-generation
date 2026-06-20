from decimal import Decimal

def subtract_values(a, b):
    return Decimal(a) - Decimal(b)

if __name__ == '__main__':
    result = subtract_values(3.141592653589793, 2.718281828459045)
    print(result)