def dollars_to_cents(amount):
    s = str(amount)
    if '.' in s:
        integer_part, fractional_part = s.split('.')
        if len(fractional_part) > 2:
            fractional_part = fractional_part[:2]
        elif len(fractional_part) == 1:
            fractional_part += '0'
        elif len(fractional_part) == 0:
            fractional_part = '00'
        return int(integer_part + fractional_part)
    else:
        return int(s) * 100

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(5.1))
    print(dollars_to_cents(10))
    print(dollars_to_cents(123.456))