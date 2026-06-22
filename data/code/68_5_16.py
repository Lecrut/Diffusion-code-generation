def dollars_to_cents(dollars):
    dollar_str = str(dollars)
    parts = dollar_str.split('.')
    integer_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else ""
    if len(fractional_part) == 0:
        fractional_part = "00"
    elif len(fractional_part) == 1:
        fractional_part += "0"
    elif len(fractional_part) > 2:
        fractional_part = fractional_part[:2]
    result_str = integer_part + fractional_part
    return int(result_str)

if __name__ == '__main__':
    print(dollars_to_cents(10.5))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(100.0))
    print(dollars_to_cents(3.1))
    print(dollars_to_cents(0.001))