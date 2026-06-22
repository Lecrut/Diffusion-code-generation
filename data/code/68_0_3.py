def dollars_to_cents(amount: float) -> int:
    return int(round(amount * 100))

if __name__ == '__main__':
    sample_amounts = [10.50, 99.99, 0.01, 100.00, 123.456, 0.005]
    for value in sample_amounts:
        print(f"{value} -> {dollars_to_cents(value)}")