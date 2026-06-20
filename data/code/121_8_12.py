import decimal

def compare_decimals(a, b):
    return a == b or a.quantize(b) == b.quantize(a)
if __name__ == '__main__':
    dec1 = decimal.Decimal('0.1')
    dec2 = decimal.Decimal('0.100000000000000005')
    result = compare_decimals(dec1, dec2)
    print(result)