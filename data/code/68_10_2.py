def dollars_to_cents(dollar_amount):
    parts = str(dollar_amount).split('.')
    dollars = int(parts[0])
    if len(parts) > 1:
        cents_part = parts[1]
        if len(cents_part) == 1:
            cents_part += '0'
        elif len(cents_part) > 2:
            cents_part = cents_part[:2]
        cents = int(cents_part)
    else:
        cents = 0
    total_cents = abs(dollars) * 100 + cents
    if dollar_amount < 0:
        total_cents = -total_cents
    return total_cents

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(0.00))
    print(dollars_to_cents(-5.67))
    print(dollars_to_cents(10.1))
    print(dollars_to_cents(100.0))