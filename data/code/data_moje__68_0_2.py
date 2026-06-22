def dollars_to_cents(amount: float) -> int:
    return int(round(amount * 100))

if __name__ == '__main__':
    test_cases = [2.0, 0.1, 0.5, 1.005, 1.015, 99.99, 0.005, 0.014]
    for val in test_cases:
        result = dollars_to_cents(val)
        print(f"dollars_to_cents({val}) = {result}")