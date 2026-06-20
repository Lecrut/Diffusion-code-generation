import operator

def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")

def perform_operations(a, b):
    operations = {
        'add': operator.add,
        'sub': operator.sub,
        'mul': operator.mul,
        'div': operator.truediv
    }
    results = {}
    for op_name, op_func in operations.items():
        try:
            validate_numbers(a, b)
            result = op_func(a, b)
        except ValueError as e:
            result = str(e)
        results[op_name] = result
    return results

if __name__ == '__main__':
    sample_values = (15, 3)
    results = perform_operations(*sample_values)
    print(results)