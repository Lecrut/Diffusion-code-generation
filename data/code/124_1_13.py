def basic_arithmetic(x, y):
    addition = x + y
    subtraction = x - y
    multiplication = x * y
    floor_division = x // y
    return {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'floor_division': floor_division
    }

if __name__ == '__main__':
    result = basic_arithmetic(7, 3)
    print(result)