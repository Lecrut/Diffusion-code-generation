def dollar_to_cents(amount):
    s = str(amount)
    if '.' in s:
        integer_part, decimal_part = s.split('.')
        if len(decimal_part) == 1:
            decimal_part += '0'
        elif len(decimal_part) > 2:
            decimal_part = decimal_part[:2]
        elif len(decimal_part) < 2:
            decimal_part += '0' * (2 - len(decimal_part))
        return int(integer_part + decimal_part)
    return int(s) * 100

if __name__ == '__main__':
    print(dollar_to_cents(10.5))
    print(dollar_to_cents(5.0))
    print(dollar_to_cents(123.45))