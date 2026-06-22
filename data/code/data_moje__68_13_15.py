def dollars_to_cents(dollar_amount):
    if not isinstance(dollar_amount, (int, float)):
        raise TypeError("Input must be a number")
    if dollar_amount < 0:
        raise ValueError("Dollar amount cannot be negative")
    return int(round(dollar_amount * 100))

if __name__ == '__main__':
    sample_values = [0.0, 1.23, 99.99, 1000.0, 0.01, 0.999]
    for value in sample_values:
        result = dollars_to_cents(value)
        print(result)