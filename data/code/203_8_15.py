import decimal

def compare_decimals(a, b):
    return a == b

if __name__ == '__main__':
    d1 = decimal.Decimal('0.1')
    d2 = decimal.Decimal('0.1')
    result = compare_decimals(d1, d2)
    print(result)