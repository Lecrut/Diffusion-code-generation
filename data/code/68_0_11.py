def dollars_to_cents(dollar_amount):
    return int(round(dollar_amount * 100))

if __name__ == '__main__':
    test_cases = [10.0, 10.01, 10.005, 0.99, 1.005, 1.006, 12.345, 0.1 + 0.2]
    for tc in test_cases:
        print(dollars_to_cents(tc))