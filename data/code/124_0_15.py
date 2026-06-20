import operator

def perform_operation(op_func, a, b):
    try:
        return op_func(a, b)
    except ZeroDivisionError:
        return "Cannot divide by zero"

if __name__ == '__main__':
    sample_values = (15, 3)
    operations = [
        (operator.add, 'Addition'),
        (operator.sub, 'Subtraction'),
        (operator.mul, 'Multiplication'),
        (operator.truediv, 'Division')
    ]
    
    results = {name: perform_operation(op_func, *sample_values) for op_func, name in operations}
    
    for name, result in results.items():
        print(f"{name}: {result}")