INT_CONST = 10
FLOAT_CONST = 5.0

def perform_arithmetic(a, b):
    results = {}
    results['addition'] = a + b
    results['subtraction'] = a - b
    results['multiplication'] = a * b
    try:
        results['division'] = a / b
    except ZeroDivisionError:
        results['division'] = 'Error: Division by zero'
    return results

def perform_float_arithmetic(a, b):
    results = {}
    results['addition'] = a + b
    results['subtraction'] = a - b
    results['multiplication'] = a * b
    try:
        results['division'] = a / b
    except ZeroDivisionError:
        results['division'] = 'Error: Division by zero'
    return results
if __name__ == '__main__':
    int_result = perform_arithmetic(INT_CONST, FLOAT_CONST)
    float_result = perform_float_arithmetic(FLOAT_CONST, INT_CONST)
    print('Integer Arithmetic Results:', int_result)
    print('Float Arithmetic Results:', float_result)