def perform_operations(a, b):
    result = {}
    result['sum'] = a + b
    result['difference'] = a - b
    result['product'] = a * b
    try:
        result['quotient'] = a / b
    except ZeroDivisionError:
        result['quotient'] = "Undefined (Division by zero)"
    return result

if __name__ == '__main__':
    sample_values = [20, 4]
    results = perform_operations(*sample_values)
    print(results)