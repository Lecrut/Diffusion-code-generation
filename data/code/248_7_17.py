def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")

def add_integers(a, b):
    validate_integer(a)
    validate_integer(b)
    return a + b

if __name__ == '__main__':
    result = add_integers(3, 5)
    print(result)