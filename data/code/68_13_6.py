def dollar_to_cents(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Input must be a number")
    return int(round(amount * 100))

if __name__ == '__main__':
    test_values = [1.23, -1.23, 0, 10.50, -0.01, 99.995]
    for val in test_values:
        result = dollar_to_cents(val)
        print(result)