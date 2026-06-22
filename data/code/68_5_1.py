def convert_to_cents(dollar_amount):
    amount_str = str(dollar_amount)
    if '.' in amount_str:
        integer_part, fractional_part = amount_str.split('.')
        if len(fractional_part) == 1:
            fractional_part += '0'
        elif len(fractional_part) > 2:
            fractional_part = fractional_part[:2]
        cents_str = integer_part + fractional_part
        return int(cents_str)
    else:
        return int(amount_str) * 100

if __name__ == '__main__':
    print(convert_to_cents(10.5))
    print(convert_to_cents(0.99))
    print(convert_to_cents(100))