ADD, SUBTRACT, MULTIPLY, DIVIDE, MODULUS = 'add', 'subtract', 'multiply', 'divide', 'modulus'

def calculate_operations(x, y):
    results = {
        ADD: x + y,
        SUBTRACT: x - y,
        MULTIPLY: x * y,
        DIVIDE: None if y == 0 else x / y,
        MODULUS: None if y == 0 else x % y
    }
    return results

if __name__ == '__main__':
    sample_values = (7, 3)
    result = calculate_operations(*sample_values)
    print(result)