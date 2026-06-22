def perform_arithmetic(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = None if b == 0 else a / b
    modulus = None if b == 0 else a % b
    return {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'modulus': modulus
    }

if __name__ == '__main__':
    sample_values = (15, 6)
    result = perform_arithmetic(*sample_values)
    print(result)