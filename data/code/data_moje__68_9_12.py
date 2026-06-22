def dollars_to_cents(dollars):
    return int(dollars * 100)

def batch_dollars_to_cents(values):
    return [dollars_to_cents(v) for v in values]

if __name__ == '__main__':
    sample_values = [1.00, 0.50, 123.45, 999.99, 0.01, 10.10]
    result = batch_dollars_to_cents(sample_values)
    print(result)