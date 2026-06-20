def perform_operations(a, b):
    result = {}
    result['sum'] = a + b
    result['difference'] = a - b
    result['product'] = a * b
    result['quotient'] = a / b if b != 0 else "Undefined (Division by zero)"
    return result

if __name__ == '__main__':
    sample_values = {'a': 20, 'b': 4}
    results = perform_operations(sample_values['a'], sample_values['b'])
    print(results)