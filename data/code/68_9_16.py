def dollars_to_cents(dollars):
    return int(dollars * 100)

def process_large_list(dollar_values):
    return [dollars_to_cents(v) for v in dollar_values]

if __name__ == '__main__':
    sample_values = [10.50, 0.99, 100.00, 42.123, 0.01, 1234.5678]
    results = process_large_list(sample_values)
    print(results)