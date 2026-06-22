def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_values = [1.0, 2.5, 0.01, 100.99, -3.14]
    results = [dollars_to_cents(v) for v in sample_values]
    print(results)