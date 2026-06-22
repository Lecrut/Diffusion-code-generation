def convert_to_cents(amount):
    s = str(amount)
    parts = s.split('.')
    if len(parts) == 1:
        integer_part = parts[0]
        fractional_part = '00'
    else:
        integer_part = parts[0]
        fractional_part = parts[1]
    if len(fractional_part) == 0:
        fractional_part = '00'
    elif len(fractional_part) == 1:
        fractional_part = fractional_part + '0'
    else:
        fractional_part = fractional_part[:2]
    total_str = integer_part + fractional_part
    return int(total_str)

if __name__ == '__main__':
    print(convert_to_cents(10.5))
    print(convert_to_cents(0.99))
    print(convert_to_cents(100))
    print(convert_to_cents(5.123))