def convert_dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_values = [10.5, 0.99, 100.0, 0.01, 1234.567, -5.25]
    for value in sample_values:
        cents = convert_dollars_to_cents(value)
        print(f"{value} -> {cents}")