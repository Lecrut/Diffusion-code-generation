def dollars_to_cents(dollar_amount):
    if not isinstance(dollar_amount, (int, float)):
        raise TypeError("Input must be a number")
    return int(dollar_amount * 100) if dollar_amount >= 0 else -int(abs(dollar_amount) * 100)

if __name__ == '__main__':
    sample_values = [10.50, -2.75, 0, 100, -0.01]
    for value in sample_values:
        print(dollars_to_cents(value))