def dollars_to_cents(amount):
    return abs(int(round(amount * 100)))

if __name__ == '__main__':
    test_values = [-12.50, 45.9, -0.01, 100.00]
    for value in test_values:
        print(dollars_to_cents(value))