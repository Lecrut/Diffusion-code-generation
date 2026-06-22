def calculate_operations(x, y):
    addition = x + y
    subtraction = x - y
    multiplication = x * y
    division = None if y == 0 else x / y
    modulus = None if y == 0 else x % y
    return {
        'add': addition,
        'subtract': subtraction,
        'multiply': multiplication,
        'divide': division,
        'modulus': modulus
    }

if __name__ == '__main__':
    sample_values = (7, 3)
    result = calculate_operations(*sample_values)
    print(result)