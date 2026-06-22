def dollars_to_cents(dollar_amount):
    if isinstance(dollar_amount, float):
        dollar_amount_str = format(dollar_amount, '.2f')
    elif isinstance(dollar_amount, int):
        dollar_amount_str = f"{dollar_amount}.00"
    elif isinstance(dollar_amount, str):
        dollar_amount_str = dollar_amount
    else:
        raise TypeError("Input must be int, float, or string")

    if '.' in dollar_amount_str:
        parts = dollar_amount_str.split('.')
        integer_part = parts[0]
        fractional_part = parts[1]
        if len(fractional_part) > 2:
            fractional_part = fractional_part[:2]
        elif len(fractional_part) < 2:
            fractional_part = fractional_part.ljust(2, '0')
    else:
        integer_part = dollar_amount_str
        fractional_part = '00'

    integer_cents = int(integer_part) * 100
    fractional_cents = int(fractional_part)
    total_cents = integer_cents + fractional_cents

    if dollar_amount_str.startswith('-') and integer_part != '0' and fractional_part == '00':
        return -total_cents

    return total_cents

if __name__ == '__main__':
    print(dollars_to_cents(123.45))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100))
    print(dollars_to_cents("99.99"))
    print(dollars_to_cents(0.1))
    print(dollars_to_cents(-50.50))