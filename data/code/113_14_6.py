from decimal import Decimal

def subtract_values(a, b):
    return Decimal(a) - Decimal(b)

if __name__ == '__main__':
    result = subtract_values(0.1, 0.2)
    print(result)