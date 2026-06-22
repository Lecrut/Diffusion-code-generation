def validate_inputs(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both inputs must be integers")

def add_integers(a, b):
    validate_inputs(a, b)
    return a + b

if __name__ == '__main__':
    result = add_integers(10, 5)
    print(f"10 + 5 = {result}")