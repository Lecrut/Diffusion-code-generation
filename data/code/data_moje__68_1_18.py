from decimal import Decimal, getcontext

def dollars_to_cents(dollars: str) -> int:
    getcontext().prec = 10
    dollars_decimal = Decimal(dollars)
    cents_decimal = dollars_decimal * Decimal('100')
    return int(cents_decimal)
if __name__ == '__main__':
    sample_values = ['1.99', '0.10', '100', '0.01', '0.123']
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)