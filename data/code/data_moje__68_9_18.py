def dollars_to_cents(dollars):
    return int(dollars * 100)

def batch_dollars_to_cents(values):
    return [int(v * 100) for v in values]

if __name__ == '__main__':
    sample_values = [1.23, 4.56, 7.89, 0.01, 100.00, 0.99, 1234.56]
    converted = batch_dollars_to_cents(sample_values)
    print(converted)
    single = dollars_to_cents(12.34)
    print(single)