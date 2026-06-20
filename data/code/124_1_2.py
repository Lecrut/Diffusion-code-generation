def basic_arithmetic(a, b):
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'floor_division': a // b
    }

if __name__ == '__main__':
    result = basic_arithmetic(10, 4)
    print(result)