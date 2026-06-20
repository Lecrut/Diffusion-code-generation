def basic_arithmetic(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    floor_division = a // b
    return {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'floor_division': floor_division
    }

if __name__ == '__main__':
    result = basic_arithmetic(12, 3)
    print(result)