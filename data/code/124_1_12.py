def basic_arithmetic(a=10, b=4):
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'floor_division': a // b
    }

if __name__ == '__main__':
    result = basic_arithmetic()
    print(result)