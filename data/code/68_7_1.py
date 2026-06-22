import decimal

def dollars_to_cents(dollars: float) -> int:
    d = decimal.Decimal(str(dollars))
    cents = d * 100
    return int(cents.to_integral_value(rounding=decimal.ROUND_HALF_UP))

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(10.00))
    print(dollars_to_cents(0.995))