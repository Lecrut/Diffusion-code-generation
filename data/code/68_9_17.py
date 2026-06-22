def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_values = [1.23, 45.67, 0.01, 100.0, 99.99]
    results = [dollars_to_cents(v) for v in sample_values]
    print(results)