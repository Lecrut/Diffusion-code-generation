def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_values = [1.0, 2.5, 10.99, 0.01, 100.0]
    for value in sample_values:
        print(dollars_to_cents(value))