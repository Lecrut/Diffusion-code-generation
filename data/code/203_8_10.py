from decimal import Decimal

def compare_decimals(d1: Decimal, d2: Decimal) -> bool:
    return d1 == d2

if __name__ == '__main__':
    dec_a = Decimal('0.1')
    dec_b = Decimal('0.10')
    result1 = compare_decimals(dec_a, dec_b)
    print(f"Comparing {dec_a} and {dec_b}: Result is {result1}")

    dec_c = Decimal('1e308')
    dec_d = Decimal('1e308')
    result2 = compare_decimals(dec_c, dec_d)
    print(f"Comparing {dec_c} and {dec_d}: Result is {result2}")