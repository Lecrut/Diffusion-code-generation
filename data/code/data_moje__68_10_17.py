def dollars_to_cents(dollars):
    if isinstance(dollars, float):
        dollars_str = f"{dollars:.2f}"
    else:
        dollars_str = str(dollars)
    if '.' in dollars_str:
        integer_part, fractional_part = dollars_str.split('.')
        fractional_part = (fractional_part + '00')[:2]
        cents = int(integer_part) * 100 + int(fractional_part)
    else:
        cents = int(dollars_str) * 100
    return cents

if __name__ == '__main__':
    sample_values = [10.00, 0.50, 123.45, 0.01, 1000.00, 1.005, 99.99]
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)