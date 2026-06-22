def dollars_to_cents(dollars):
    if isinstance(dollars, int):
        return dollars * 100
    elif isinstance(dollars, float):
        cents_str = f"{dollars:.2f}".rstrip('0').rstrip('.')
        if '.' in cents_str:
            whole, frac = cents_str.split('.')
            frac = frac.ljust(2, '0')
            return int(whole + frac)
        else:
            return int(cents_str) * 100
    elif isinstance(dollars, str):
        if '.' in dollars:
            whole, frac = dollars.split('.')
            frac = frac.ljust(2, '0')[:2]
            return int(whole + frac)
        else:
            return int(dollars) * 100
    else:
        raise TypeError("Input must be int, float, or string representing dollars")

if __name__ == '__main__':
    sample_values = [
        10.5,
        0.01,
        100,
        123.456,
        "50.5",
        "0.01",
        10.00,
        -10.5,
        0,
        1.999
    ]
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)