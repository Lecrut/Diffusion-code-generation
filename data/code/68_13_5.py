def dollars_to_cents(amount: float) -> int:
    return int(amount * 100)

if __name__ == '__main__':
    sample_values = [5.99, 100.00, -12.34, 0.01, 0.0]
    for value in sample_values:
        result = dollars_to_cents(value)
        print(f"{value} -> {result}")