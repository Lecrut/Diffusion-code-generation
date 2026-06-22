def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_values = [1.0, 10.50, 0.99, 500.0]
    for val in sample_values:
        print(dollars_to_cents(val))