import operator

NUM1 = 15
NUM2 = 3

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
    results = perform_operations(NUM1, NUM2)
    for op, result in results.items():
        print(f"{op}: {result}")