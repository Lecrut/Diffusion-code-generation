def dollars_to_cents(dollar_amount):
    return int(round(dollar_amount * 100))

if __name__ == '__main__':
    sample_values = [1.00, 0.99, 10.005, 10.015, 123.456, 0.001, 999999.999, -1.234, -0.005]
    for val in sample_values:
        print(dollars_to_cents(val))