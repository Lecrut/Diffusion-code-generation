def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_values = [10.00, 5.50, 0.99, 123.45, 0.01]
    for value in sample_values:
        result = dollars_to_cents(value)
        print(f"{value} -> {result}")