def perform_operations(a, b):
    result = {}
    result['sum'] = a + b
    result['difference'] = a - b
    result['product'] = a * b
    result['quotient'] = a / b if b != 0 else "Undefined (Division by zero)"
    return result

if __name__ == '__main__':
    sample_values = [20, 4]
    results = perform_operations(sample_values[0], sample_values[1])
    print(results)