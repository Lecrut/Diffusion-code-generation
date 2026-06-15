def perform_arithmetic(a, b, c):
    results = {}
    results['addition'] = a + b
    results['subtraction'] = a - b
    results['multiplication'] = a * b
    try:
        results['division'] = a / b
    except ZeroDivisionError:
        results['division'] = "Error: Division by zero"
    return results
if __name__ == '__main__':
    a_val = 10
    b_val = 2
    c_val = 5
    output = perform_arithmetic(a_val, b_val, c_val)
    print(output)
    a_val = 10
    b_val = 0
    c_val = 5
    output = perform_arithmetic(a_val, b_val, c_val)
    print(output)