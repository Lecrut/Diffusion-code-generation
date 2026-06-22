from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def dollars_to_cents(dollars):
    if isinstance(dollars, (int, float)):
        dollars = Decimal(str(dollars))
    elif isinstance(dollars, str):
        try:
            dollars = Decimal(dollars)
        except InvalidOperation:
            raise ValueError(f"Invalid dollar value: {dollars}")
    elif not isinstance(dollars, Decimal):
        raise TypeError(f"Unsupported type: {type(dollars)}")
    
    cents = (dollars * 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return int(cents)

if __name__ == '__main__':
    print(dollars_to_cents(1.00))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(1.99))
    print(dollars_to_cents(10.5))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100.00))
    print(dollars_to_cents("12.34"))
    print(dollars_to_cents(Decimal("99.99")))
    print(dollars_to_cents(0.1 + 0.2))