import operator

def perform_operations(a, b):
    operations = {
        'add': operator.add,
        'sub': operator.sub,
        'mul': operator.mul,
        'div': lambda x, y: (x / y) if y != 0 else None
    }
    
    results = {op: operations[op](a, b) for op in operations}
    return results

if __name__ == '__main__':
    result = perform_operations(15, 3)
    print(result)