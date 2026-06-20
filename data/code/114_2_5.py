from decimal import Decimal, getcontext
getcontext().prec = 50

def multiply_decimals(a, b):
    return Decimal(a) * Decimal(b)
if __name__ == '__main__':
    result = multiply_decimals(0.1, 0.2)
    print(result)