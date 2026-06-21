import decimal

def compare_decimals(a, b):
    return a == b

if __name__ == '__main__':
    dec1 = decimal.Decimal('0.1')
    dec2 = decimal.Decimal('0.1')
    print(compare_decimals(dec1, dec2))