def dollar_to_cents(dollars):
    return round(dollars * 100)

if __name__ == '__main__':
    test_values = [10.00, 10.005, 10.004, 10.01, 0.995]
    for val in test_values:
        print(dollar_to_cents(val))