def dollars_to_cents(dollars: float) -> int:
    cents = int(round(dollars * 100))
    return cents

if __name__ == '__main__':
    sample_values = [1.25, 10.00, 0.99, 5.55, 0.01]
    for value in sample_values:
        result = dollars_to_cents(value)
        print(f"{value} -> {result}")