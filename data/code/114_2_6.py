def multiply_decimals(a, b):
    from decimal import Decimal
    return Decimal(a) * Decimal(b)
if __name__ == '__main__':
    sample_a = 0.123456789
    sample_b = 9876543.21
    result = multiply_decimals(sample_a, sample_b)
    print(result)