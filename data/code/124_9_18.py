def validate_input(data):
    if len(data) != 2:
        raise ValueError("Input list must contain exactly two elements")

def perform_operations(a, b):
    result = {}
    result['a'] = a
    result['b'] = b
    result['sum'] = a + b
    result['difference'] = a - b
    result['product'] = a * b
    result['quotient'] = a / b if b != 0 else "Undefined (Division by zero)"
    return result

if __name__ == '__main__':
    sample_values = [20, 4]
    validate_input(sample_values)
    results = perform_operations(*sample_values)
    print(results)