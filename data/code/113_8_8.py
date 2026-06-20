def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return a, b

def subtract(a, b):
    a, b = validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    print(subtract(10, 5))
    print(subtract(5, 10))
    print(subtract(10, 10))
    print(subtract(-5, 3))
    print(subtract(3, -5))
    print(subtract(-10, -5))
    print(subtract(-10, -10))