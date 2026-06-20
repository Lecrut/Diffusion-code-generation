import operator

def perform_operations(a, b):
    operations = {
        'add': operator.add,
        'sub': operator.sub,
        'mul': operator.mul,
        'div': operator.truediv
    }
    
    results = {}
    for op_name, func in operations.items():
        try:
            result = func(a, b)
        except ZeroDivisionError:
            result = "Cannot divide by zero"
        results[op_name] = result
    
    return results

if __name__ == '__main__':
    a = 15
    b = 3
    results = perform_operations(a, b)
    for op, result in results.items():
        print(f"{op.capitalize()}: {result}")