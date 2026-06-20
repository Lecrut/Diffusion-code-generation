def multiply_decimals(a, b):
    from decimal import Decimal, getcontext
    getcontext().prec = 28
    return float(Decimal(a) * Decimal(b))

if __name__ == '__main__':
    a = 0.1
    b = 0.2
    result = multiply_decimals(a, b)
    print(result)