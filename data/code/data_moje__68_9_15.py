import sys

def convert_dollars_to_cents(values):
    return [int(v * 100) for v in values]

if __name__ == '__main__':
    sample_values = [10.50, 0.99, 100.00, 5.25, 0.01]
    result = convert_dollars_to_cents(sample_values)
    print(result)