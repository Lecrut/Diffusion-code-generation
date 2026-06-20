import decimal

def multiply_decimals(a, b):
    return a * b

if __name__ == '__main__':
    result = multiply_decimals(decimal.Decimal('2.5'), decimal.Decimal('4.2'))
    print(result)