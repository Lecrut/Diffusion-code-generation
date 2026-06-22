def dollars_to_cents(dollars: float) -> int:
    return int(round(dollars * 100))

if __name__ == '__main__':
    test_values = [10.50, 0.99, 1.005, 100.00, -5.25]
    for value in test_values:
        print(dollars_to_cents(value))