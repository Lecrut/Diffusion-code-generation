def dollar_to_cents(dollar_amount):
    amount_str = str(dollar_amount)
    if '.' in amount_str:
        integer_part, fractional_part = amount_str.split('.')
        fractional_part = fractional_part.ljust(2, '0')[:2]
        cents = int(integer_part) * 100 + int(fractional_part)
    else:
        cents = int(amount_str) * 100
    return cents

if __name__ == '__main__':
    dollars = [99.99, 0.5, 100.0, 1234.56]
    for dollar in dollars:
        print(dollar_to_cents(dollar))