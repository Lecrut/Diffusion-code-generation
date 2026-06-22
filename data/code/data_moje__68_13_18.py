def dollars_to_cents(dollar_amount):
    if not isinstance(dollar_amount, (int, float)):
        raise TypeError("Input must be a number")
    return int(dollar_amount * 100)

if __name__ == '__main__':
    sample_values = [10.50, -5.25, 0, 100.0, -0.01]
    for value in sample_values:
        result = dollars_to_cents(value)
        print(result)