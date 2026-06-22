def dollars_to_cents(dollars):
    if isinstance(dollars, float):
        dollars_str = f"{dollars:.2f}"
        parts = dollars_str.split(".")
        dollar_part = parts[0]
        cent_part = parts[1] if len(parts) > 1 else "00"
        if len(cent_part) < 2:
            cent_part = cent_part + "0" * (2 - len(cent_part))
        elif len(cent_part) > 2:
            cent_part = cent_part[:2]
        total_cents = int(dollar_part) * 100 + int(cent_part)
        return total_cents
    elif isinstance(dollars, int):
        return dollars * 100
    else:
        raise TypeError("Input must be an integer or float")

if __name__ == '__main__':
    print(dollars_to_cents(10))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(100.10))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(1234.56))