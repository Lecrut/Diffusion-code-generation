def perform_arithmetic(a, b):
    operations = {
        'addition': lambda x, y: x + y,
        'subtraction': lambda x, y: x - y,
        'multiplication': lambda x, y: x * y,
        'division': lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    results = {op: operations[op](a, b) for op in operations}
    return results

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    output = perform_arithmetic(num1, num2)
    print(output)