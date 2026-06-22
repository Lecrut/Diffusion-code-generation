def dollar_to_cents(dollar_value):
    return int(round(dollar_value * 100))

if __name__ == '__main__':
    sample_values = [10.5, 10.49, 10.51, 0.005, 100.0]
    for val in sample_values:
        print(dollar_to_cents(val))