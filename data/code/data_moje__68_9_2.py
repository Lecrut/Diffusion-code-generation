def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_values = [10.50, 0.99, 100.00, 0.01, 25.75]
    results = [dollars_to_cents(d) for d in sample_values]
    print(results)