def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    test_values = [10.5, -2.75, 0.01, -0.01, 100.0, -50.55]
    for value in test_values:
        print(dollars_to_cents(value))