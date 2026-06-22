def dollars_to_cents(dollars):
    if isinstance(dollars, float):
        return int(round(dollars * 100))
    if isinstance(dollars, int):
        return dollars * 100
    if isinstance(dollars, str):
        if '.' in dollars:
            parts = dollars.split('.')
            if len(parts) != 2:
                raise ValueError("Invalid dollar format")
            int_part = int(parts[0])
            frac_part = parts[1]
            if len(frac_part) == 1:
                frac_part += '0'
            elif len(frac_part) > 2:
                frac_part = frac_part[:2]
            cents = int_part * 100 + int(frac_part)
            return cents if not dollars.startswith('-') else -cents
        else:
            return int(dollars) * 100
    raise TypeError("Unsupported type")

if __name__ == '__main__':
    test_values = [10.50, 10.0, 0.99, 100, 10.999, -5.5]
    for val in test_values:
        result = dollars_to_cents(val)
        print(result)