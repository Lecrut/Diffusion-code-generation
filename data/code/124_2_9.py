import math

def calculate_operations(a=25.5, b=4.2):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    modulus = a % b
    power = math.pow(a, b)
    square_root_a = math.sqrt(a)
    square_root_b = math.sqrt(b)

    return {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'division': division,
        'modulus': modulus,
        'power': power,
        'square_root_a': square_root_a,
        'square_root_b': square_root_b
    }

if __name__ == '__main__':
    results = calculate_operations()
    for key, value in results.items():
        print(value)