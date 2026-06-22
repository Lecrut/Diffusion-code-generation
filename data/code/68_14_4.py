def convert_dollars_to_cents(dollars):
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number")
    total_cents = int(dollars * 100)
    return total_cents

if __name__ == '__main__':
    test_values = [10, 5.50, 0.25, 100, 99.99]
    for value in test_values:
        print(convert_dollars_to_cents(value))