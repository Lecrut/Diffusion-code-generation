def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")

def add(a, b):
    validate_integer(a)
    validate_integer(b)
    return a + b

def subtract(a, b):
    validate_integer(a)
    validate_integer(b)
    return a - b

if __name__ == '__main__':
    print(add(5, 3))
    print(subtract(10, 4))