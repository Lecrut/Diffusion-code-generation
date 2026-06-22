def dollars_to_cents(amount):
    rounded_amount = round(amount * 100)
    return int(rounded_amount)

if __name__ == '__main__':
    test_values = [10.0, 10.99, 10.005, 12.345, 0.01, 0.009, -5.50, 100.0]
    for value in test_values:
        result = dollars_to_cents(value)
        print(f"{value} -> {result}")