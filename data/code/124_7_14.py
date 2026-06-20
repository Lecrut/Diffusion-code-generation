if __name__ == '__main__':
    x = 12
    y = 3
    operations = {
        'sum': lambda: x + y,
        'difference': lambda: x - y,
        'product': lambda: x * y,
        'quotient': lambda: x / y,
        'modulus': lambda: x % y
    }
    results = {op: operations[op]() for op in operations}
    print(f"Sum: {results['sum']}, Difference: {results['difference']}, Product: {results['product']}, Quotient: {results['quotient']}, Modulus: {results['modulus']}")