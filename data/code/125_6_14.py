def validate_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")

def add(a, b):
    validate_integers(a, b)
    return a + b

def subtract(a, b):
    validate_integers(a, b)
    return a - b

if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))