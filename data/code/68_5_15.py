def dollars_to_cents(dollars):
    dollar_str = str(dollars)
    if '.' in dollar_str:
        parts = dollar_str.split('.')
        integer_part = parts[0]
        fractional_part = parts[1][:2].ljust(2, '0')
        combined = integer_part + fractional_part
    else:
        combined = dollar_str + '00'
    return int(combined)

if __name__ == '__main__':
    print(dollars_to_cents(1.23))
    print(dollars_to_cents(0.5))
    print(dollars_to_cents(10))
    print(dollars_to_cents(0.001))
    print(dollars_to_cents(100.999))