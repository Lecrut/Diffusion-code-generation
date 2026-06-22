def dollars_to_cents(dollars):
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number")
    return int(round(dollars * 100))

if __name__ == '__main__':
    test_values = [1.0, 1.23, 0.29, 100.00, 0.005, 0.004]
    for val in test_values:
        print(dollars_to_cents(val))