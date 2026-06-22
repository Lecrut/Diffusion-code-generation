def dollar_to_cents(amount):
    return abs(int(round(amount * 100)))

if __name__ == '__main__':
    test_values = [10.50, -3.75, 0, -0.01, 99.999]
    for val in test_values:
        print(dollar_to_cents(val))