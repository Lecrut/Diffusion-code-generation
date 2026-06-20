import operator

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
            result = op_func(a, b)
        except ZeroDivisionError:
            result = "Cannot divide by zero"
        results[op_name] = result
    return results

if __name__ == '__main__':
    sample_values = (15, 3)
    results = perform_operations(*sample_values)
    print(results)