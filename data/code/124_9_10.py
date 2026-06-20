def perform_operations(a, b):
    operations = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'quotient': None if b == 0 else a / b
    }
    return operations

if __name__ == '__main__':
    sample_values = [20, 4]
    results = perform_operations(*sample_values)
    print(results)