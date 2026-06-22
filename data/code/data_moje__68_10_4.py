def dollars_to_cents(dollars_str):
    if '.' in dollars_str:
        integer_part, fractional_part = dollars_str.split('.')
        fractional_part = fractional_part.ljust(2, '0')[:2]
        return int(integer_part) * 100 + int(fractional_part)
    else:
        return int(dollars_str) * 100

if __name__ == '__main__':
    print(dollars_to_cents("12.34"))
    print(dollars_to_cents("0.05"))
    print(dollars_to_cents("100"))
    print(dollars_to_cents("0.1"))