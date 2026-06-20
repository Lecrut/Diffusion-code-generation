import operator

def calculate_operations(a, b):
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
    a = 15
    b = 3
    results = calculate_operations(a, b)
    for op, result in results.items():
        print(f"{op.capitalize()}: {result}")