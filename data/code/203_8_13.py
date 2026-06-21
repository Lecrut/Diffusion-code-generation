import decimal

def compare_decimals(d1, d2):
    return d1 == d2

if __name__ == '__main__':
    sample_decimal_1 = decimal.Decimal('0.1')
    sample_decimal_2 = decimal.Decimal('0.1')
    result = compare_decimals(sample_decimal_1, sample_decimal_2)
    print(f"Comparing {sample_decimal_1} and {sample_decimal_2}: Result is {result}")