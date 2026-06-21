from decimal import Decimal

def validate_decimal(obj):
    if not isinstance(obj, Decimal):
        raise ValueError("Input must be an instance of Decimal")

def compare_decimals(d1, d2):
    validate_decimal(d1)
    validate_decimal(d2)
    
    return d1 == d2

if __name__ == '__main__':
    dec_a = Decimal('0.1')
    dec_b = Decimal('0.10')
    result1 = compare_decimals(dec_a, dec_b)
    print(f"Comparing {dec_a} and {dec_b}: Result is {result1}")
    
    dec_c = Decimal('12345678901234567890.1234567890')
    dec_d = Decimal('12345678901234567890.1234567890')
    result2 = compare_decimals(dec_c, dec_d)
    print(f"Comparing {dec_c} and {dec_d}: Result is {result2}")