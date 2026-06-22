from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def dollars_to_cents(dollars):
    if isinstance(dollars, str):
        dollars_decimal = Decimal(dollars)
    elif isinstance(dollars, (int, float)):
        dollars_decimal = Decimal(str(dollars))
    elif isinstance(dollars, Decimal):
        dollars_decimal = dollars
    else:
        raise TypeError("Input must be a string, int, float, or Decimal")
    
    cents = dollars_decimal * 100
    return int(cents.to_integral_value(rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    print(dollars_to_cents("12.345"))
    print(dollars_to_cents(10.00))
    print(dollars_to_cents("0.01"))
    print(dollars_to_cents(Decimal("99.99")))
    print(dollars_to_cents("-5.555"))