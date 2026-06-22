from decimal import Decimal, ROUND_HALF_UP

def dollars_to_cents(dollars: float) -> int:
    decimal_value = Decimal(str(dollars))
    cent_value = (decimal_value * 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return int(cent_value)

if __name__ == '__main__':
    print(dollars_to_cents(10.99))
    print(dollars_to_cents(0.1))
    print(dollars_to_cents(0.2))
    print(dollars_to_cents(0.3))