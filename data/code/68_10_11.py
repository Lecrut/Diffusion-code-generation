def dollars_to_cents(dollars_str):
    if isinstance(dollars_str, str):
        dollars_str = dollars_str.replace(',', '')
        if '.' in dollars_str:
            whole_part, fractional_part = dollars_str.split('.')
            fractional_part = (fractional_part + '00')[:2]
            cents = int(whole_part) * 100 + int(fractional_part)
        else:
            cents = int(dollars_str) * 100
    else:
        cents = int(dollars_str) * 100
    return cents

if __name__ == '__main__':
    print(dollars_to_cents("123.45"))
    print(dollars_to_cents("0.01"))
    print(dollars_to_cents("1000.00"))
    print(dollars_to_cents("5.5"))
    print(dollars_to_cents("10.999"))