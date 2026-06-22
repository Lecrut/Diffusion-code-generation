NUMBERS = (10, 5)

def calculate_operations(x, y):
    ADD = x + y
    SUBTRACT = x - y
    MULTIPLY = x * y
    DIVIDE = None if y == 0 else x / y
    MODULUS = None if y == 0 else x % y
    return {
        'add': ADD,
        'subtract': SUBTRACT,
        'multiply': MULTIPLY,
        'divide': DIVIDE,
        'modulus': MODULUS
    }

if __name__ == '__main__':
    result = calculate_operations(*NUMBERS)
    print(result)