def convert_dollars_to_cents(amounts):
    return [int(d * 100) for d in amounts]

if __name__ == '__main__':
    sample_values = [1.25, 10.00, 0.99, 50.55, 0.01, 100.00]
    result = convert_dollars_to_cents(sample_values)
    print(result)