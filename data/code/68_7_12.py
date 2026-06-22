def dollars_to_cents(dollars):
    return int(round(dollars * 100, 0))

if __name__ == '__main__':
    test_cases = [1.25, 1.255, 0.999, 10.0, -2.5]
    for value in test_cases:
        print(dollars_to_cents(value))