def arithmetic_operations(a, b, c):
    results = {}
    results['sum'] = a + b + c
    results['difference'] = a - b
    results['product'] = a * b
    try:
        results['division'] = a / b
    except ZeroDivisionError:
        results['division'] = "Undefined (Division by zero)"
    return results
if __name__ == '__main__':
    a_val = 10
    b_val = 2
    c_val = 5
    output = arithmetic_operations(a_val, b_val, c_val)
    print(output)