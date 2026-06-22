def dollars_to_cents(dollar_amount):
    integer_part = int(dollar_amount)
    fractional_part = abs(dollar_amount) - abs(integer_part)
    fractional_cents = round(fractional_part * 100)
    total_cents = integer_part * 100 + fractional_cents
    if dollar_amount < 0 and fractional_cents > 0:
        total_cents -= 100 + fractional_cents
    return total_cents

if __name__ == '__main__':
    sample_values = [0, 1, -1, 1.5, -1.5, 10.00, 10.01, 10.99, 0.01, 0.005, 0.004, 0.995, 0.994, 123.456, -123.456]
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)