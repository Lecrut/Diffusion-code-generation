def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a + b

def subtract(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a - b

if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))