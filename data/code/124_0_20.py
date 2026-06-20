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
            results[op_name] = result
        except ZeroDivisionError:
            results[op_name] = "ZeroDivisionError"
    
    return results

if __name__ == '__main__':
    a = 15
    b = 3
    results = perform_operations(a, b)
    print(results)