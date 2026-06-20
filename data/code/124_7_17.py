operations = {
    'sum': lambda x, y: x + y,
    'difference': lambda x, y: x - y,
    'product': lambda x, y: x * y,
    'quotient': lambda x, y: x / y if y != 0 else None,
    'modulus': lambda x, y: x % y
}

def calculate_results(x, y):
    results = {op: operations[op](x, y) for op in operations}
    return results

if __name__ == '__main__':
    x = 12
    y = 3
    result = calculate_results(x, y)
    print(f"Sum: {result['sum']}, Difference: {result['difference']}, Product: {result['product']}, Quotient: {result['quotient']}, Modulus: {result['modulus']}")