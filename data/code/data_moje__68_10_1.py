def dollars_to_cents(dollar_amount):
    if isinstance(dollar_amount, int):
        return dollar_amount * 100
    elif isinstance(dollar_amount, float):
        return int(round(dollar_amount * 100))
    elif isinstance(dollar_amount, str):
        parts = dollar_amount.split('.')
        if len(parts) == 1:
            return int(parts[0]) * 100
        else:
            dollars = int(parts[0])
            cents_part = parts[1]
            if len(cents_part) == 0:
                cents = 0
            elif len(cents_part) == 1:
                cents = int(cents_part) * 10
            else:
                cents = int(cents_part[:2])
            return dollars * 100 + cents
    else:
        raise TypeError("Unsupported type")

if __name__ == '__main__':
    print(dollars_to_cents(10))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(1.0))
    print(dollars_to_cents("123.45"))
    print(dollars_to_cents(99.99))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(0))
    print(dollars_to_cents("-5.50"))