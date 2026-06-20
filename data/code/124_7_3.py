operations = {
    'sum': lambda x, y: x + y,
    'difference': lambda x, y: x - y,
    'product': lambda x, y: x * y,
    'quotient': lambda x, y: x / y if y != 0 else None,
    'modulus': lambda x, y: x % y
}

if __name__ == '__main__':
    x = 12
    y = 3
    results = {op: operations[op](x, y) for op in operations}
    print(f"Sum: {results['sum']}, Difference: {results['difference']}, Product: {results['product']}, Quotient: {results['quotient']}, Modulus: {results['modulus']}")