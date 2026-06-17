def arithmetic_operations(a, b, c):
    results = {}
    results['addition'] = a + b
    results['subtraction'] = a - b
    results['multiplication'] = a * b
    if b != 0:
        results['division'] = a / b
    else:
        results['division'] = "Division by zero error"
    return results
if __name__ == '__main__':
    a_val = 10
    b_val = 2
    c_val = 5
    output = arithmetic_operations(a_val, b_val, c_val)
    print(output)