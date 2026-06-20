def calculate_operations(x, y):
    return {
        'sum': x + y,
        'difference': x - y,
        'product': x * y,
        'quotient': x / y if y != 0 else None,
        'modulus': x % y
    }

if __name__ == '__main__':
    x = 12
    y = 3
    results = calculate_operations(x, y)
    print(f"Sum: {results['sum']}, Difference: {results['difference']}, Product: {results['product']}, Quotient: {results['quotient']}, Modulus: {results['modulus']}")