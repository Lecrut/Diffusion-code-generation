def dollar_to_cents(dollar_amount):
    dollar_str = str(dollar_amount)
    if '.' in dollar_str:
        integer_part, fractional_part = dollar_str.split('.')
        fractional_part = fractional_part.ljust(2, '0')[:2]
        cents_str = integer_part + fractional_part
    else:
        cents_str = dollar_str + '00'
    if dollar_str.startswith('-'):
        return -int(cents_str)
    return int(cents_str)

if __name__ == '__main__':
    print(dollar_to_cents(12.34))
    print(dollar_to_cents(0.99))
    print(dollar_to_cents(5))
    print(dollar_to_cents(-10.50))